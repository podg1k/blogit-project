# urls.py -- leads
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_page, name='contact_page'),
]