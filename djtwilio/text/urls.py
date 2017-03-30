from django.conf.urls import url, include
from django.contrib import admin
from text import views

urlpatterns = [
    url(r'^sms/$', views.sms),
    # url(r'^ring/$', 'views.ring()'),
]
