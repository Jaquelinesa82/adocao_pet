from django.db import models
from base.models import User


class Pet(models.Model):
    city = models.CharField(max_length=100)
    description = models.TextField( )
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    end_date = models.DateTimeField(null=True, blank=True)
    begin_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    file = models.ImageField(upload_to='pet', blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pet'
