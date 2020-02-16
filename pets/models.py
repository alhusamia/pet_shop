from django.db import models
from django.urls import reverse
class Pet(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10 ,decimal_places=2)
    def get_absolute_url(self):
        return reverse('pet-detail', args=[str(self.id)])
