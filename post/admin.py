from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin

from .models import *

# Register your models here.
admin.site.register(Travel, GeoModelAdmin)
admin.site.register(Post)
admin.site.register(View)
