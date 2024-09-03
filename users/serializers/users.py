"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate

# Django REST Frameork
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User model serilizer."""

    class Meta:
        """Meta class."""

        model = User
        fields = ("username", "first_name", "last_name", "email")


class UserSingUpSerializer(serializers.ModelSerializer):
    """User sign up model serializer.

    Handle sign up data validation and user creation."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        min_length=4, max_length=20, validators=[UniqueValidator]
    )
    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    # Name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify passwords match."""
        passwd = data["password"]
        passwd_conf = data["password_confirmation"]

        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")

        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop("password_confirmation")
        user = User.objects.create_user(**data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """User Login Serializer.

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=4, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        self.context["user"] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context["user"], token.key
