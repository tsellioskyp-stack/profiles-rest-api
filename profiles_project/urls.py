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
# ewithin their respective applications. After loading some Viewsets, the api root will be http://localhost:8000/api/ and it will show
# the available endpoints, such as http://localhost:8000/api/hello-viewset/ and http://localhost:8000/api/hello-view/. Here it displays ONLY the
# endpoints that are registered with the router, and not the ones that are defined as class-based views, like the HelloApiView,
# which is why we need to add a separate URL pattern for it in the urls.py file of the profiles_api application.
# Could i override this and display in the api root page, the APIVIEWS also? Yes, you can override the default API root
# view provided by Django REST Framework to include both the ViewSet endpoints and the APIView endpoints. To do this,
# you can create a custom API root view and include it in your URL patterns. Here's how you can do it:
# 1. Create a custom API root view in your views.py file:
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# class CustomApiRootView(APIView):
#     def get(self, request, format=None):
#         api_root = {
#             'hello-viewset': reverse('hello-viewset-list', request=request, format=format),
#             'hello-view': reverse('hello-view', request=request, format=format),
#         }
#         return Response(api_root)
# 2. Then, in your urls.py file, include the custom API root view:
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from profiles_api import views
# router = DefaultRouter()
# router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
# urlpatterns = [
#     path("", views.CustomApiRootView.as_view(), name='api-root'),
#     path("hello-view/", views.HelloApiView.as_view(), name='hello-view'),
#     path("", include(router.urls)),
# ]
# In this example, we created a CustomApiRootView that returns a response containing the URLs for both the hello-viewset and the hello-view.
# We then included this view in our URL patterns, making it the default endpoint for the API root. Now, when you access
# http://localhost:8000/api/, you will see both the ViewSet and APIView endpoints listed.
