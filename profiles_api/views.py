from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import reverse, status
from rest_framework import viewsets

from profiles_api import serializers


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
