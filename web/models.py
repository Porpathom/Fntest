from django.db import models

SEX_CHOICES = [
    (1,'ชาย'),
    (2,'หญิง'),
]

EDUCATION_CHOICES = [
    (1,'ปวช.'),
    (2,'ปวส.'),
    (3,'ปริญญาตรี'),
    (4,'สูงกว่าปริญญาตรี')
]

# Create your models here.

class Department(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name

class Employ(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.IntegerField(choices=SEX_CHOICES, default=1)
    age = models.CharField(max_length=25)
    education = models.IntegerField(choices=EDUCATION_CHOICES, default=None)
    dep =models.ForeignKey(Department, on_delete=models.CASCADE,default=None)
    
    class Meta:
        verbose_name = "Employ"
        verbose_name_plural = "Employs"

    def __str__(self):
        return self.first_name + " "+self.last_name




