from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.utils import json
from rest_framework.views import APIView
from .models import DocumentKey, Blogs, Contact
from .serializer import BlogSerializer, ContactSerializer, DocumentKeySerializer
import requests


# Create your views here.

def api(request, id):
    if id is not None:
        if id == "354fe0f8":
            return render(request, 'api/index.html')
        else:
            return HttpResponse("404 Error Please Request Admin For API Key")
    else:
        return HttpResponse("404 Error Page Not Found")


def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        email = request.POST.get('email')
        data = {"name": title, "email": email, "comment": comment}
        headers = {"Content-Type": "application/json"}
        response = requests.post('http://127.0.0.1:8000/api/contactsapi/', json=data, headers=headers)
        print(response)
    return render(request, 'api/index.html')


def detail(request):
    return render(request, 'api/Details.html')


def portfolio(request):
    return render(request, 'api/Portfolio.html')


def document(request):
    data = {}
    confirm = ""
    if request.method == "POST":

        key = request.POST.get('key')
        for getkey in DocumentKey.objects.all():
            print(getkey)
            if getkey.key == key:
                data = {'confirmation': 'true'}
                break
            else:
                data = {'confirmation': 'false'}

    return render(request, 'api/Document.html', data)


# API Code

class BlogApiView(APIView):
    def get(self, request, id=None, format=None):
        if id is not None:
            blog = Blogs.objects.get(id=id)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        blogs = Blogs.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg:Blog Added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        blog = Blogs.objects.get(id=id)
        serializer = BlogSerializer(blog, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Update'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id, format=None):
        # id = pk
        blog = Blogs.objects.get(id=id)
        serializer = BlogSerializer(blog, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data patch'})
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        blog = Blogs.objects.get(id=id)
        blog.delete()
        return Response({'msg': 'Data Deleted'})


class ContactApi(APIView):
    def get(self, request, format=None):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg:Contact Added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentKeyApi(APIView):
    def get(self, request, format=None):
        d_key = DocumentKey.objects.all()
        serializer = DocumentKeySerializer(d_key, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DocumentKeySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg:Document Key Add'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
