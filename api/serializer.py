from rest_framework import serializers
from .models import Blogs, Contact, DocumentKey


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
