from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(SocialLink)
admin.site.register(Notification)
admin.site.register(Friendship)
