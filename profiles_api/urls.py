from django.urls import path
from profiles_api import views

urlpatterns = [path("hello-view/", views.HelloApiView.as_view())]
# This line defines a URL pattern for the "hello-view/" endpoint. When a request is made to this URL, it will be handled by the HelloApiView
# class-based view defined in the views module of the profiles. This site wil be accessed not by going to http://localhost:8000/hello-view/
# but by going to http://localhost:8000/api/hello-view/ because we included the profiles_api.urls in the main urls.py file with the prefix "api/".
