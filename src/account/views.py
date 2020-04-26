from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView

from account.models import User
from account.forms import SignUpForm, CustomUserEditForm


def smoke(request):
    return HttpResponse('smoke')


'''
Create profile app (first name, last name, data of birth, biography, contacts).
Add front page, where you'll show your profile data (use fixtures).

Add authentication for this page.

Create a page where you may change your profile.
'''


class UserInfoView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    template_name = 'SignUP.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('account:user-info')
    form_class = SignUpForm


class EditUserView(UpdateView):
    template_name = 'edit.html'
    form_class = CustomUserEditForm
    queryset = User.objects.all()
    success_url = reverse_lazy('account:user-info')


