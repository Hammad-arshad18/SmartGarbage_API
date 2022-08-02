from django.contrib import admin
from .models import Blogs, Contact, DocumentKey, EmployeeTask, Employee, TaskStatus,userTasks


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


@admin.register(EmployeeTask)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_data', 'employee']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'status']


@admin.register(userTasks)
class userTaskAdmin(admin.ModelAdmin):
    list_display = ['id']