from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime   

class Pet(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    HEALTH_STATUS_CHOICES = [
        ('vaccinated', 'Vaccinated'),
        ('spayed', 'Spayed'),
        ('neutered', 'Neutered'),
        ('medical_conditions', 'Medical Conditions'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets', null=True)  # Associate pet with a user
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)
    color = models.CharField(max_length=30)  # New field for color
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)  # New field for size with dropdown options
    health_status = models.CharField(max_length=20, choices=HEALTH_STATUS_CHOICES)  # New field for health status with dropdown options
    posted_date = models.DateTimeField(default=datetime.now, blank=True)  # New field for posted date (auto set to current date when created)
    adoption_fee = models.DecimalField(max_digits=8, decimal_places=2)  # New field for adoption fee


    def __str__(self):
        return self.name
