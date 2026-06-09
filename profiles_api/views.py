from rest_framework.views import APIView, PermissionDenied
from rest_framework.response import Response
from rest_framework import reverse, status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method": "PUT"})
        # Where the request is the data sent by the client, and pk is the primary key of the object to update

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({"method": "PATCH"})
        # Where the request is the data sent by the client, and pk is the primary key of the object to update

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"method": "DELETE"})
        # Where the request is the data sent by the client, and pk is the primary key of the object to delete


class HelloViewSet(viewsets.ViewSet):
    # This is a viewset, and it does not use the APIView class, but it uses the ViewSet class from the rest_framework.viewsets module
    # A custom HelloViewSet class is created, which inherits from the ViewSet class, and it is used to handle the HTTP methods
    # for the APIView
    """Test API ViewSet"""
    serializer_class = (
        serializers.HelloSerializer
    )  # THis creates a form in the webpage, a "window" to type in

    # In contrast to APIView, which maps HTTP methods to functions, a ViewSet maps actions (list, create, retrieve, update, partial_update,
    # destroy) to functions already defined in the ViewSet class, and we only need to define the functions for the actions we want to handle
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            phone_number = serializer.validated_data.get("phone_number")
            is_active = serializer.validated_data.get("is_active")
            message = f"Hello {name}! Your phone number is {phone_number} and you are {'active' if is_active else 'not active'}."
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(
        self, request, pk=None
    ):  # The pk is the primary key of the object to retrieve, and it is passed as an argument to the function, and it is used to get the object from the database. It is passed in the URL of the request, and it is used to identify the object to retrieve.
        """Handle getting an object by its ID"""
        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({"http_method": "DELETE"})


class ByeByeViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = (
        serializers.ByeByeSerializer
    )  # THis creates a form in the webpage, a "window" to type in

    def list(self, request):
        """Return a bye message"""
        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Bye!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a new bye message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Bye {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # DRF takes care of all the CRUD operations for us, and we only need to specify the serializer class and the queryset for the viewset. The ModelViewSet class provides default implementations for the list, create, retrieve, update, partial_update, and destroy actions, which are all we need to handle the CRUD operations for our user profiles. By specifying the serializer class and the queryset, we can easily create an API that allows us to create, retrieve, update, and delete user profiles without having to write any additional code for these operations.
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnProfile,
    )  # This line specifies the permission classes that will be used to determine whether a user has permission to perform certain actions on the user profiles. In this case, we are using a custom permission class called UpdateOwnProfile, which is defined in the permissions.py file. This permission class allows users to edit their own profile, but not other users' profiles. By including this permission class in the UserProfileViewSet, we can ensure that users can only update their own profiles and not those of other users, providing an additional layer of security for our API.
    filter_backends = (
        filters.SearchFilter,
    )  # This line specifies the filter backends that will be used to enable searching and filtering of user profiles in the API. In this case, we are using the SearchFilter backend provided by Django REST Framework, which allows us to search for user profiles based on specific fields. By including this filter backend in the UserProfileViewSet, we can enable searching for user profiles based on their name and email fields, making it easier for clients to find specific user profiles in the API. The search_fields attribute specifies the fields that can be searched, and in this case, we are allowing searching by name and email, which are common fields that users may want to search for when looking for specific user profiles. On the URL, it will be something like http://localhost:8000/api/profile/?search=John, and it will return all the user profiles that have "John" in their name or email.
    search_fields = ("name", "email")


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    # This line specifies the renderer classes that will be used to render the response for the user login API view. By default, the ObtainAuthToken view provided by Django REST Framework does not include any renderer classes, which means that it will not render any response when a user logs in. By setting the renderer_classes attribute to api_settings.DEFAULT_RENDERER_CLASSES, we are enabling the default renderer classes provided by Django REST Framework, which include JSONRenderer and BrowsableAPIRenderer. This allows us to receive a response in JSON format when a user logs in, which can be useful for clients that need to parse the response and extract the authentication token for subsequent API requests. Additionally, it also allows us to use the browsable API interface provided by Django REST Framework, which can be helpful for testing and debugging our API during development.


class ProfileFeedItemViews(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        IsAuthenticated,
        permissions.UpdateOwnStatus,
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
        # This method is called when a new profile feed item is created through the API. It takes the serializer as an argument, which contains the data for the new profile feed item being created. The method then calls the save() method on the serializer, passing in the user_profile argument with the value of self.request.user. This sets the user_profile field of the new profile feed item to the currently logged-in user, ensuring that each status update is associated with a specific user profile in our API. By doing this, we can easily track which user created each status update and provide personalized content for each user based on their profile information.

        # If the user is not authenticated or does not have permission to create a profile feed item
