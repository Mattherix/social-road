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

    @property
    def url(self):
        if self.network == 'F':
            return 'https://www.facebook.com/' + self.username
        elif self.network == 'Y':
            return 'https://www.youtube.com/user/' + self.username
        elif self.network == 'I':
            return 'https://www.instagram.com/' + self.username + '/'
        elif self.network == 'Tw':
            return 'https://twitter.com/' + self.username
        elif self.network == 'S':
            return 'snapchat://add/' + self.username
        elif self.network == 'P':
            return 'https://www.pinterest.fr/' + self.username + '/'
        elif self.network == 'L':
            return 'https://www.linkedin.com/in/' + self.username
        elif self.network == 'Te':
            return 'https://t.me/' + self.username
        elif self.network == 'R':
            return 'https://www.reddit.com/user/' + self.username


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

    def accept(self):
        """Accepté une demande d'amitié"""
        self.validate = True
