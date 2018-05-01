from django.conf.urls import include, url
from .views import *
from django.urls import path
urlpatterns = [
    url(r'^update/$', UpdateAPI.as_view()),
]