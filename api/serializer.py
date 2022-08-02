from rest_framework import serializers
from .models import Blogs, Contact, DocumentKey, Employee, TaskStatus, userTasks, changePassword


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class DocumentKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentKey
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'


class EmployeeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = userTasks
        fields = '__all__'


class changePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = changePassword
        fields = '__all__'
