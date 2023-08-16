from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    student_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    email=models.EmailField()
    join_date=models.DateField()
    qualification=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    number=models.IntegerField(max_length=10)
   