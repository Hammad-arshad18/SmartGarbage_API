from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.utils import json
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import DocumentKey, Blogs, Contact, EmployeeTask, Employee, TaskStatus, userTasks
from .serializer import BlogSerializer, ContactSerializer, DocumentKeySerializer, EmployeeSerializer, TaskSerializer, \
    EmployeeTaskSerializer
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


def hammad(request):
    return render(request, 'api/hammad.html')


def wahab(request):
    return render(request, 'api/wahab.html')


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


# Employee Api
class UserTask(APIView):
    def get(self, request, format=None):
        getTaskEmployees = userTasks.objects.all()
        serializer = EmployeeTaskSerializer(getTaskEmployees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = EmployeeTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            adduserTask()
            return Response("Task Added SuccessFully")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def adduserTask():
    userTask = userTasks.objects.all()
    employeeTask = EmployeeTask.objects.all()
    for i in userTask:
        # print(i.username)
        if EmployeeTask.objects.count() > 0:
            try:
                employeeTask = EmployeeTask.objects.get(task_data=i.task_data)
            except EmployeeTask.DoesNotExist:
                employeeTask = None
                if employeeTask is None:
                    taskNew = EmployeeTask(task_data=i.task_data)
                    taskNew.save()
        else:
            # print(i.id)
            taskNew = EmployeeTask(task_data=i.task_data)
            taskNew.save()


class EmployeeApi(APIView):
    def get(self, request, uname=None, format=None):
        addEmployees()
        if uname is not None:
            employee = Employee.objects.filter(username=uname)
            serializer = EmployeeSerializer(employee, many=True)
            return Response(serializer.data)
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def patch(self, request, uname=None, format=None):
        if id is not None:
            employee = Employee.objects.get(username=uname)
            tasksEmployee = employee.tasks
            tasksEmployee += 1
            jsonData = {"tasks": tasksEmployee}
            serializer = EmployeeSerializer(employee, jsonData, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response('Employee Update', status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To Filter &  Employees From User Main Table
def addEmployees():
    allUsers = User.objects.all()
    allEmployees = Employee.objects.all()
    for i in allUsers:
        # print(i.username)
        if i.is_superuser:
            continue
        else:
            if Employee.objects.count() > 0:
                try:
                    getEmployee = Employee.objects.get(username=i.username)
                except Employee.DoesNotExist:
                    getEmployee = None
                    if getEmployee is None:
                        employeeNew = Employee(username=i.username, email=i.email)
                        employeeNew.save()
            else:
                employeeNew = Employee(username=i.username, email=i.email)
                employeeNew.save()


# Employee Task Api

class Task(APIView):
    def get(self, request, uname=None, format=None):
        addTask()
        if uname is not None:
            task = TaskStatus.objects.filter(username=uname)
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)
        tasks = TaskStatus.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def patch(self, request, uname=None, format=None):
        task = TaskStatus.objects.get(username=uname)
        serializer = TaskSerializer(task, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Update Successfully")


def addTask():
    employeeTask = EmployeeTask.objects.all()
    taskStatus = TaskStatus.objects.all()
    for i in employeeTask:
        # print(i.username)
        if TaskStatus.objects.count() > 0:
            try:
                taskStatus = TaskStatus.objects.get(taskid=i.id)
            except TaskStatus.DoesNotExist:
                taskStatus = None
                if taskStatus is None:
                    taskNew = TaskStatus(task_data=i.task_data, username=i.employee, taskid=i.id)
                    taskNew.save()
        else:
            # print(i.id)
            taskNew = TaskStatus(task_data=i.task_data, username=i.employee, taskid=i.id)
            taskNew.save()


# Employee of The Month/Year API
class EmployeeAward(APIView):
    def get(self, request, format=None):
        awardEmployee = Employee.objects.all().order_by('tasks').last()
        serializer = EmployeeSerializer(awardEmployee)
        return Response(serializer.data)
