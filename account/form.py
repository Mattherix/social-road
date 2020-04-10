from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models.user import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

