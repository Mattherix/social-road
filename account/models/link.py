"""Models lié directement à l'utilisateur mais aussi à d'autre models"""
from django.db import models

from .user import User


class SocialLink(models.Model):
    """Lien sociaux de l'utilisateur

    Ce model représente les liens des reseaux sociaux de l'utilisateur
        date: Date de création de l'object
        user: Un lien vers le models de l'utilisateur integré dans Django
        network: Le réseau social
        username: Le nom d'utilisateur dans le réseau social
    """
    date = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    NETWORK = (
        ('F', 'facebook'),
        ('Y', 'youtube'),
        ('I', 'instagram'),
        ('Tw', 'twitter'),
        ('S', 'snapchat'),
        ('P', 'pinterest'),
        ('L', 'linkedIn'),
        ('Te', 'telegram'),
        ('R', 'reddit'),
    )
    network = models.CharField(max_length=2, choices=NETWORK)
    username = models.CharField(max_length=300)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.user.username + ' is ' + self.username + ' on ' + self.network


class Friendship(models.Model):
    """Lien d'amitié

    Ce model représente un lien d'amitié entre 2 utilisateur:
        date: Date de création de l'object
        creator: Créateur de la demande
        friend: Amis demandé
        notification: Notification lié
        validate: La demande a elle été accepté True/False
    """
    date = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')
    validate = models.BooleanField(default=False)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.creator.username + ' ❤️ ' + self.friend.username
