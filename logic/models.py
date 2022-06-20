from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    location = models.CharField(max_length=50, null=False)
    police = models.IntegerField(null=True)
    health = models.IntegerField(null=True)
    handyman = models.IntegerField(null=True)
    # occupants = models.IntegerField(default=0)
    admin = models.ForeignKey(
        User, null=False, related_name='neighbourhoods', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="users", on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(
        Neighbourhood, related_name="occupants", on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.user.username
