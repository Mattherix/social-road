from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.gis.db import models

from account.models import User


class Travel(models.Model):
    """Chemin effectué par un utilisateur

    Ce model représente un parcours fait par l'utilisateur:
        date: Date de création de l'object
        creator: Créateur du trajet
        travel: Trajet effectué
    """
    date = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    travel = models.MultiLineStringField(geography=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return str(self.date) + ' ' + str(self.creator)


class Post(models.Model):
    """Post d'un utilisateur

    Ce model représente un post fait par un utilisateur:
        date: Date de création de l'object
        creator: Créateur du post
        title: Le titre du post
        text: Le texte du post
    """
    date = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = RichTextUploadingField(blank=True)
    travel = models.OneToOneField(Travel, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return str(self.creator) + ' ' + str(self.date) + '  ' + self.text[:100]


class View(models.Model):
    """Vue d'un utilisateur

    Ce model représente un post fait par un utilisateur:
        date: Date de création de l'object
        user: User qui a vue
        post: Le post lier à la vue
        like: Le post est-il like ?
        total: Nombre foit ou l'utilisateur à vue le post
    """
    date = models.DateTimeField(auto_now_add=True, editable=False)

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    like = models.BooleanField()
    total = models.IntegerField()

    class Meta:
        ordering = ('date',)

    def __str__(self):
        if self.like:
            like = 'like'
        else:
            like = "don't like"
        return self.user.username + ' have seen ' + str(self.total) + ' time ' + str(self.post) + ' and ' + \
            like + ' it'
