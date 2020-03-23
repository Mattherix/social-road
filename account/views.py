from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .models import Friendship, Notification


def register_view(request):
    return render(request, 'account/register.html')


def login_view(request):
    return render(request, 'account/login.html')


@login_required()
def logout_view(request):
    return HttpResponse('Déconnecté')


@login_required()
def edit_view(request):
    return render(request, 'account/edit.html')


@method_decorator(login_required, name='get')
class FriendList(ListView):
    model = Friendship
    template_name = 'account/friends.html'
    context_object_name = 'friend_list'
    paginate_by = 1


@method_decorator(login_required, name='get')
class NotificationList(ListView):
    model = Notification
    template_name = 'account/notification.html'
    context_object_name = 'notification_list'