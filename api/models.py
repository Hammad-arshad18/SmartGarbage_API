from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel


# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    postDetails = models.TextField(max_length=2500, blank=False, null=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    comment = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name + " (" + self.email + " )"


class DocumentKey(models.Model):
    key = models.CharField(max_length=20, blank=False, null=False)


# class User(AbstractUser):
#     email = models.EmailField(unique=True)

class Employee(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    tasks = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.username


class TaskStatus(models.Model):
    task_data = models.CharField(max_length=200)
    status = models.CharField(max_length=100, null=True, blank=True, default="Pending")
    username = models.CharField(max_length=200)
    taskid=models.IntegerField(default=0)

    def __str__(self):
        return self.status


class EmployeeTask(models.Model):
    task_data = models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    # status=models.CharField(max_length=100, null=True, blank=True, default="Pending")



# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserModel.objects.get(username=username)
#         except UserModel.DoesNotExist:
#             try:
#                 user = UserModel.objects.get(email=username)
#             except UserModel.DoesNotExist:
#                 # Run the default password hasher once to reduce the timing
#                 # difference between an existing and a nonexistent user (#20760).
#                 UserModel().set_password(password)
#             else:
#                 if user.check_password(password) and self.user_can_authenticate(user):
#                     return user
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user
