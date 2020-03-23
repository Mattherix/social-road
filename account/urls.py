from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('edit', views.edit_view, name='edit'),
    path('friends', views.FriendList.as_view(), name='friends'),
    path('notifications', views.NotificationList.as_view(), name='notifications')
]