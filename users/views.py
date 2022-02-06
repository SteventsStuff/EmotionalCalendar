from django.contrib.auth import views
from django.shortcuts import reverse
from django.views import generic

from .forms import CustomSignupForm


class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomSignupForm

    def get_success_url(self):
        return reverse('signin')


class SigninView(views.LoginView):
    template_name = 'registration/signin.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('home')
