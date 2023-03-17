from django.contrib import admin
from django.urls import path
from rail_pic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.railpic, name='railpic'),
]
