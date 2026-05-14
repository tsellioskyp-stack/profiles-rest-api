from rest_framework import serializers
from django.core.validators import RegexValidator

letters_only = RegexValidator(
    regex=r"^[a-zA-Z]+$", message="Only letters are allowed."
)  # A custom validator that ensures that the input
# for the name field only contains letters. The regex pattern r"^[a-zA-Z]+$" means that the input must start (^) and end ($)
# with one or more (+) letters (a-z and A-Z). If the input does not match this pattern,
# it will raise a validation error with the message "Only letters are allowed."


class HelloSerializer(serializers.Serializer):
    # Means, create new class called HelloSerializer that inherits from the Serializer class provided by the Django REST Framework serializers module.
    # This class will be used to define the structure of the data that we want to serialize and validate for our API view.
    """Serializes a name field for testing our APIView. What it will do is, by inputting a name, it will serialize that name
    and return it back to us in the API response, in the HelloAPIView. This is just a simple example to demonstrate how serializers work in Django REST Framework.
    """

    name = serializers.CharField(
        max_length=10, validators=[letters_only]
    )  # CharField means that the name field will accept string input, and max_length=10
    #   means that the maximum length of the name can be 10 characters. If we try to input a name longer than 10 characters,
    # it will raise a validation error. This serializer will be used in our API view to validate the input data and serialize it
    # before sending it back in the response.
