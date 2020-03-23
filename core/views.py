from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from account.models import User

def index(request):
    return render(request, 'home.html')


def license(request):
    return render(request, 'license.html')


def privacy(request):
    return render(request, 'privacy.html')


@method_decorator(login_required, name='get')
class ProfileDetail(DetailView):
    model = User
    template_name = 'profile.html'
