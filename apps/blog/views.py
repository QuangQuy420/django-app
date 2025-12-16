from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Post


class PostLockMixin:
    def get_lock_key(self):
        return f"lock_post_{self.kwargs['pk']}"

    def get(self, request, *args, **kwargs):
        """
        Runs when user clicks 'Edit/Delete' and sees the confirmation page.
        We must acquire the lock here to prevent others from editing while we decide.
        """
        lock_key = self.get_lock_key()
        current_holder = cache.get(lock_key)

        # Case 1: Locked by someone else
        if current_holder and current_holder != request.user.id:
            messages.error(
                request,
                f"Cannot delete: This post is currently being edited/locked by User ID {current_holder}.",
            )
            return redirect("blog:post_list")

        # Case 2: Free (or locked by me) -> Take/Renew the lock
        # We use a short timeout (e.g., 300s) for the confirmation screen
        cache.set(lock_key, request.user.id, timeout=300)

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Runs when the user clicks 'Confirm' button on the delete page.
        """
        lock_key = self.get_lock_key()
        current_holder = cache.get(lock_key)

        # Safety Check: Did the lock expire or get stolen?
        if current_holder and current_holder != self.request.user.id:
            messages.error(
                self.request,
                "Action failed: Your lock expired and someone else is editing this post.",
            )
            return redirect("blog:post_list")

        # Proceed with deletion
        response = super().form_valid(form)

        # Clean up: Remove the lock (even though the post is gone, it's good hygiene)
        cache.delete(lock_key)

        return response


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_posts = context["posts"]  # The posts currently on this page

        # 1. Create a map of {RedisKey: PostID} for all visible posts
        # Example: {'lock_post_1': 1, 'lock_post_2': 2}
        key_map = {f"lock_post_{p.pk}": p.pk for p in page_posts}

        # 2. Fetch ALL locks from Redis in one single network call (Efficient!)
        # Returns dictionary of {key: user_id} for keys that exist
        active_locks = cache.get_many(key_map.keys())

        # 3. Identify which posts are locked by OTHER users
        # We store these IDs in a set for fast lookup in the template
        locked_ids = set()
        current_user_id = self.request.user.id

        for key, holder_id in active_locks.items():
            if holder_id != current_user_id:
                # Get the original Post ID from our map
                post_id = key_map[key]
                locked_ids.add(post_id)

        context["locked_post_ids"] = locked_ids
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, PostLockMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")


class PostDeleteView(LoginRequiredMixin, PostLockMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")

    def get_queryset(self):
        # Ensure users can only delete their own posts
        return super().get_queryset().filter(author=self.request.user)
