from django.conf import settings
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, UpdateView

from account.form import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm
from .models import Friendship, Notification, User


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
    return redirect('core:index')


@method_decorator(login_required, name='get')
class EditView(UpdateView):
    template_name = 'account/edit.html'
    form_class = CustomUserChangeForm
    model = User
    success_url = settings.LOGIN_REDIRECT_URL

    def get_object(self, queryset=None):
        return self.request.user

    def get(self, request, **kwargs):
        self.object = User.objects.get(pk=self.request.user.pk)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


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
