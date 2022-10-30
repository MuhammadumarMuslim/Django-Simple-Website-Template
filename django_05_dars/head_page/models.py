from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phono_number = models.IntegerField()
    password = models.CharField(max_length=10)
    course_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
