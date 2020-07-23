from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"
