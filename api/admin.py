from django.contrib import admin
from .models import Blogs, Contact, DocumentKey


# Register your models here.
# admin.site.register(Blogs)

@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'postDetails']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


@admin.register(DocumentKey)
class DocumentKeyAdmin(admin.ModelAdmin):
    list_display = ['id', 'key']


