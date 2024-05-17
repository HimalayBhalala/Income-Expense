from django.db import models
from app.models import User

# Create your models here.

class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('Online Service','Online Service'),
        ('Travel','Travel'),
        ('Food','Food'),
        ('Rent','Rent'),
        ('Others','Others')
    )
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=20)
    amount = models.DecimalField(max_digits=10,max_length=10,decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.owner} 's Expense"