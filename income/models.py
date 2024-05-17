from django.db import models
from app.models import User

# Create your models here.

class Income(models.Model):
    SOURCE_CATEGORY = (
        ('Salary','Salary'),
        ('Business','Business'),
        ('Others','Others'),
    )

    source = models.CharField(choices=SOURCE_CATEGORY,max_length=10)
    amount = models.DecimalField(max_digits=10,max_length=10,decimal_places=2)
    description = models.TextField()
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    date = models.DateField(auto_created=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.owner} 's income"