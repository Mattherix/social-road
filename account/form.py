from django.contrib.auth.forms import UserCreationForm

from .models.user import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date')
