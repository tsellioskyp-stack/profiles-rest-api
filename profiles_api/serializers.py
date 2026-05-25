from rest_framework import serializers
from django.core.validators import RegexValidator
from profiles_api import models

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

    phone_number = serializers.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
            )
        ],
    )  # CharField for phone number, with a regex validator to ensure that the input is in the correct format. The regex pattern r"^\+?1?\d{9,15}$" means that the phone number can optionally start with a plus sign (+) and an optional country code (1), followed by 9 to 15 digits. If the input does not match this pattern, it will raise a validation error with the message "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    is_active = serializers.BooleanField(
        default=False
    )  # A boolean field to indicate if the user is active or not. The default value is True, meaning that by default, all users will be considered active unless specified otherwise.


class ByeByeSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView. What it will do is, by inputting a name, it will serialize that name
    and return it back to us in the API response, in the HelloAPIView. This is just a simple example to demonstrate how serializers work in Django REST Framework.
    """

    name = serializers.CharField(
        max_length=10, validators=[letters_only]
    )  # CharField means that the name field will accept string input, and max_length=10


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:  # A configuration class that tells the serializer which model to use and which fields to include in the serialized output. In this case, we are using the UserProfile model from our models.py file, and we are including the id, email, name, phone_number, is_active, and is_black fields in the serialized output. The extra_kwargs option is used to specify additional keyword arguments for the fields. In this case, we are setting the password field to be write-only, meaning that it will not be included in the serialized output when retrieving user profiles, but it can be used when creating or updating user profiles.
        model = models.UserProfile
        fields = (
            "id",
            "email",
            "password",
            "name",
            "phone_number",
            "is_active",
            "is_black",
            "tester",
        )
        read_only_fields = (
            "tester",
        )  # What fields to be accessible in the API. The id field is included to provide a unique identifier for each user profile, which can be useful for retrieving, updating, or deleting specific user profiles through the API. The email, name, phone_number, is_active, and is_black fields are included to provide relevant information about the user profiles in the API responses. These fields are created in the models.py file, and they represent the attributes of the user profiles that we want to expose through the API.
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"},
            }  # style is used to specify the input type for the password field in the API documentation, making it clear that this field should be treated as a password input.
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
            phone_number=validated_data.get("phone_number"),
            is_black=validated_data.get("is_black"),
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)
