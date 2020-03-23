from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('new', views.new_post, name='new_post'),
    path('all', views.PostList.as_view(), name='posts'),
    path('<int:pk>', views.PostDetail.as_view(), name='post'),
]
