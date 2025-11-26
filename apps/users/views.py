from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

from .serializers import RegisterSerializer, LoginSerializer


# ------------------------------
# Register View
# ------------------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# ------------------------------
# Login View (JWT)
# ------------------------------
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        # generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "tokens": {
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }
        })


# ------------------------------
# Logout (blacklist refresh token)
# ------------------------------
class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()           # requires simplejwt blacklist app
            return Response({"detail": "Logged out successfully"})
        except Exception:
            return Response({"detail": "Invalid token"}, status=400)


# ------------------------------
# Get current user profile
# ------------------------------
class ProfileView(generics.RetrieveAPIView):
    serializer_class = RegisterSerializer   # reuse fields
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
