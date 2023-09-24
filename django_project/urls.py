"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appdoEnzo import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("locals/create", views.create_lived),
    path("locals/update/<id>", views.update_lived),
    path("locals/delete/<id>", views.delete_lived),
    path("schools/create", views.create_school),
    path("schools/update/<id>", views.update_school),
    path("schools/delete/<id>", views.delete_school),
    path('admin/', admin.site.urls),
]
