from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy', views.privacy, name='privacy'),
    path('license', views.license, name='license'),
    path('<slug:slug>', views.ProfileDetail.as_view(), name='profile')
]
