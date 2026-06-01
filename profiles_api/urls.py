from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register("bye-bye-viewset", views.ByeByeViewSet, basename="bye-bye-viewset")
router.register(
    "profile", views.UserProfileViewSet, basename="profile"
)  # This registers the UserProfileViewSet with the router, which automatically generates URL patterns for the viewset. The basename argument is optional in this case because the viewset is a ModelViewSet and it can automatically determine the base name from the queryset. The generated URL patterns for the UserProfileViewSet will be prefixed with "profile". For example, the list action of the UserProfileViewSet will be accessible at http://localhost:8000/api/profile/ and the detail action for a specific user profile will be accessible at http://localhost:8000/api/profile/<id>/, where <id> is the unique identifier of the user profile.

urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view(), name="login"),
    path("", include(router.urls)),
]
# This line defines a URL pattern for the "hello-view/" endpoint. When a request is made to this URL, it will be handled by the HelloApiView
# class-based view defined in the views module of the profiles. This site wil be accessed not by going to http://localhost:8000/hello-view/
# but by going to http://localhost:8000/api/hello-view/ because we included the profiles_api.urls in the main urls.py file with the prefix "api/".
# Also the router.register line registers the HelloViewSet with the router, which automatically generates URL patterns for the viewset.
# The basename argument is used to specify a base name for the generated URL patterns, which is useful when you have multiple viewsets
# that may have overlapping names. In this case, the generated URL patterns for the HelloViewSet will be prefixed with "hello-viewset".
# For example, the list action of the HelloViewSet will be accessible at http://localhost:8000/api/hello-viewset/.
