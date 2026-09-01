from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    skills = models.TextField()
    projects = models.TextField(blank=True)
    certifications = models.TextField(blank=True)

    def __str__(self):
        return self.name;