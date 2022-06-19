from django.db import models


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
