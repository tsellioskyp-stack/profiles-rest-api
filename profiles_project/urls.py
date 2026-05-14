"""profiles_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path(
        "admin/", admin.site.urls
    ),  # Admin URL that is by default provided by Django for administrative tasks.
    # It allows you to manage your application's data through a web interface.
    path(
        "api/", include("profiles_api.urls")
    ),  # Added for my custom API. This line includes the URL patterns defined in the profiles_api
    # application. Any additional URL patterns defined in the profiles_api/urls.py file will be prefixed with "api/". For example, if you have a
    # URL pattern defined as path("hello-view/", views.HelloApiView.as_view()) in profiles_api/urls.py, it will be accessible at
    #  http://localhost:8000/api/hello-view/. If we create a new class api view, let's say "GoodbyeApiView" and add a URL pattern for it
    #  in profiles_api/urls.py, it will also be accessible under the "api/" prefix, such as http://localhost:8000/api/goodbye-view/.
]  # In simple words, the urls.py file in the profiles_project directory serves as the main URL configuration for the entire project,
# while the urls.py file in the profiles_api directory is responsible for handling URLs specific to the profiles_api application.
# By including the profiles_api.urls in the main urls.py file with a prefix, we can organize our URL patterns and keep them modular
# ewithin their respective applications.
