"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import Group
from django.conf import settings
from django.utils import timezone

# Django REST Frameork
import jwt.exceptions
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from users.models import User

# Utilities
import jwt
from datetime import timedelta

# Serializers
from .human_resourse import HumanResourceModelSerializer


class GroupSerializer(serializers.ModelSerializer):
    """Serializador de grupos."""

    class Meta:
        model = Group
        fields = ["id", "name"]


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    human_resource = HumanResourceModelSerializer(
        read_only=True
    )  # Agregar Human Resource
    groups = GroupSerializer(many=True, read_only=True)  # Agregar grupos

    class Meta:
        """Meta class."""

        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_staff",
            "is_active",
            "is_verified",
            "human_resource",  # Devolver human resource al frontend
            "groups",  # Devolver grupos al frontend
        ]


class UserSingUpSerializer(serializers.Serializer):
    """User sign up model serializer.

    Handle sign up data validation and user creation."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
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
        user = User.objects.create_user(**data, is_verified=False)
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        """Send account verification link to given user."""
        verification_token = self.get_verification_token(user)
        subject = "Welcome @{}! Verify your account to strar using Flow Tasks".format(
            user.username
        )
        from_email = "Task Flow <acorderofigueroa7@gmail.com>"
        content = render_to_string(
            "emails/users/account_virification.html",
            {"token": verification_token, "user": user},
        )
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()

        print("Sending email.")

    def get_verification_token(self, user):
        """Create JWT token that the user can use to verify its account."""
        exp_date = timezone.now() + timedelta(days=3)
        payload = {
            "user": user.username,
            "exp": int(exp_date.timestamp()),
            "type": "email_confirmation",
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token


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
        if not user.is_verified:
            raise serializers.ValidationError("Account is not active yet :(")

        self.context["user"] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context["user"], token.key


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer."""

    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid."""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.exceptions.ExpiredSignatureError:
            raise serializers.ValidationError("Verification link has expired.")
        except jwt.exceptions.PyJWTError:
            raise serializers.ValidationError("Invalid token.")

        if payload["type"] != "email_confirmation":
            raise serializers.ValidationError("Invalid token.")

        self.context["payload"] = payload
        return data

    def save(self):
        """Update user's verified status."""
        payload = self.context["payload"]
        user = User.objects.get(username=payload["user"])
        user.is_verified = True
        user.save()
