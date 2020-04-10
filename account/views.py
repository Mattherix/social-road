from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView

from account.form import CustomUserCreationForm, CustomAuthenticationForm
from .models import Friendship, Notification


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = CustomUserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = CustomAuthenticationForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


@login_required()
def logout_view(request):
    logout(request)
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
    template_name = 'account/notifications.html'
    context_object_name = 'notification_list'
