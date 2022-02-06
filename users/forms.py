from django.contrib.auth import forms

from . import models


class CustomSignupForm(forms.UserCreationForm):

    class Meta:
        model = models.User
        # todo: ???
        fields = ('username',)
        field_classes = {'username': forms.UsernameField}
