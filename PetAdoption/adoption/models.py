from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets', null=True)# Associate pet with a user
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)  # New field for the pet photo

    def __str__(self):
        return self.name
