from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="Homepage"),
    # path('api/<str:id>', views.api, name="API"),
    path('details/', views.detail, name="Details"),
    path('document/', views.document, name='Document'),
    path('portfolio/', views.portfolio, name='Portfolio'),
    #     Api EndPoints
    path('api/blogsapi/', views.BlogApiView.as_view()),
    path('api/blogsapi/<int:id>/', views.BlogApiView.as_view()),
    path('api/contactsapi/', views.ContactApi.as_view()),
    path('api/documentkeyapi/', views.ContactApi.as_view()),
    # Api Authentication
    path('api/auth/accounts/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/account/', include('allauth.urls'))
]
