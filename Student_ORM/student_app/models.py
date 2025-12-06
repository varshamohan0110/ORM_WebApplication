from django.db import models
from django.contrib import admin
# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    enrollment_date = models.DateField()

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'enrollment_date']
