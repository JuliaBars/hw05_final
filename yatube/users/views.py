from __future__ import annotations

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm

""" Настраиваем отображение нашей формы на странице регистрации"""


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'
