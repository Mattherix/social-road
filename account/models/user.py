"""Models lié à l'utilisateur seul"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Profile de l'utilisateur

    Ce model représente tous ce qui est lier à l'utilisateur et qui n'a pas de model
        date: Date de création de l'object
        user: Un lien vers le models de l'utilisateur integré dan Django
        slug: Un bout d'url, le profile de l'utilisateur est à <ip>:<port>/<slug>
        bio: Une courte biographie de l'utilisateur
        birth: Date de naissance
        image: L'image de profile de l'utilisateur
    """
    date = models.DateTimeField(auto_now_add=True, editable=False)

    slug = models.SlugField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='profile/%Y/%m/%d', default='profile/default.png')

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.username
