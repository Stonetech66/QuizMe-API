import uuid
from django.urls import reverse
from django.db import models
from django.contrib.auth.models  import AbstractUser

# Create your models here.

class User(AbstractUser):
    id=models.UUIDField(editable=False, unique=True, primary_key=True, default=uuid.uuid4)
    email=models.EmailField(unique=True)
    username=models.CharField(unique=True, max_length=90)


    def get_answers_url(self):
        return reverse("all-users-answers", kwargs={"pk":self.id})