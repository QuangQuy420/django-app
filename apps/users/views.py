from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.users.forms import CustomUserCreationForm

User = get_user_model()


# ------------------------------
# Register View
# ------------------------------
class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")   


# ------------------------------
# Login View
# ------------------------------
class LoginView(FormView):
    template_name = "users/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


# ------------------------------
# Logout
# ------------------------------
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("users:login")


# ------------------------------
# Get current user profile
# ------------------------------
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"
