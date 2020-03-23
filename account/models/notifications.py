from django.db import models

from post.models import Post
from .user import User


class Notification(models.Model):
    """Notification de l'utilisateur

    Ce model représente une notification pour un utilisateur:
        date: Date de création de l'object
        user: Un lien  er le profile de l'utilisateur
        post: Le post lier à la notification (optionnel)
        type: Le type de notification
        level: Un entier de 1 à 10 (les 2 bornes inclues) sur l'importance du message
        message: le message de la notification
    """
    date = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    TYPE = (
        ('S', 'system'),  # Notification téchenique (ex: Adresse email qui a fuiter sur haveibeenpwned)
        ('N', 'news'),  # Message des propriétaire
        ('P', 'post'),  # New post
        ('F', 'friend'),  # Demande d'amis
        ('C', 'comment'),  # Commentaire
        ('S', 'suggestion')  # Suggestion de post ou amis
    )
    type = models.CharField(max_length=1, choices=TYPE)
    level = models.IntegerField()
    message = models.CharField(max_length=200)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.message
