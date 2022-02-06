from django.contrib.auth import models as contrib_models
from django.db import models


class User(contrib_models.AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
