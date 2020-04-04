"""Models lié à l'utilisateur seul"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class User(AbstractUser):
    """Profile de l'utilisateur

    Ce model représente tous ce qui est lier à l'utilisateur et qui n'a pas de model
        date: Date de création de l'object
        slug: Un bout d'url, le profile de l'utilisateur est à <ip>:<port>/<slug>
        bio: Une courte biographie de l'utilisateur
        birth: Date de naissance
        image: L'image de profile de l'utilisateur
        username: Le nom d'utilisateur
        email: Email de l'utilisateur
        Et tous les autres attributs d'AbstractUser
    """
    date = models.DateTimeField(auto_now_add=True, editable=False)

    slug = models.SlugField(blank=True, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='profile/%Y/%m/%d', default='profile/default.png')

    class Meta:
        ordering = ('date',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
