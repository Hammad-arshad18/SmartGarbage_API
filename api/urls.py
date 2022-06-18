from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Homepage"),
    path('api/<str:id>', views.api, name="API"),
    path('details/', views.detail, name="Details"),
    path('document/', views.document, name='Document'),

]
