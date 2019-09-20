from django.db import models

# Create your models here.
class Seven(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    height=models.DecimalField(max_digits=5,decimal_places=2)
    birthday=models.DateField()