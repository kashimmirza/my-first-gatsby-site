from django.db import models

from django.contrib.postgres.fields import ArrayField

# packages required for Person Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Department(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)

class Course(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.CharField(max_length=64)

class Section(models.Model):
    no = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Face(models.Model):
    time = models.DateField(auto_now=True)
    url = models.URLField(unique=True, null=False)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PID = models.CharField(max_length=16)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_person(sender, instance, **kwargs):
    instance.person.save()

class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    sectionList = ArrayField(
        models.IntegerField()
    )
    faceList = ArrayField(
        models.IntegerField()
    )


class Faculty(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    sectionList = ArrayField(
        models.IntegerField()
    )

class ReadingMaterial(models.Model):
    time = models.DateField(auto_now=True)
    url = models.URLField(unique=True, null=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    section = ArrayField(
        models.IntegerField()
    )

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    type = models.CharField(max_length=64, null=False)
    def __str__(self):
        return self.file.name
