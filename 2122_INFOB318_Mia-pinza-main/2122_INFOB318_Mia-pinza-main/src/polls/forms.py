
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class User_registration(UserCreationForm):
    """
    cette class crée un formulaire pour l'inscription d'un utilisateur sur le site
    """

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
