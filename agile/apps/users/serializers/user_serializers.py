# apps/users/serializers.py

import re
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.users.models import User
from apps.users.choices.positions import Positions

class UserListSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'position',
            'email',
            'phone',
            'last_login',
            'project',
        )

class UserDetailSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'position',
            'project',
        )

class RegisterUserSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'position',
            'password',
            're_password',
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'position': {'required': True},
        }

    def validate(self, data):
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        position = data.get('position')

        if not re.match('^[a-zA-Z0-9_]*$', username):
            raise serializers.ValidationError({"username": "The username must be alphanumeric characters or have only _ symbol"})

        if not re.match('^[a-zA-Z]*$', first_name):
            raise serializers.ValidationError({"first_name": "The first name must contain only alphabet symbols"})

        if not re.match('^[a-zA-Z]*$', last_name):
            raise serializers.ValidationError({"last_name": "The last name must contain only alphabet symbols"})

        if position not in [pos.name for pos in Positions]:  # Validate position against Enum
            raise serializers.ValidationError({"position": "Invalid position."})

        password = data.get("password")
        re_password = data.get("re_password")

        if password != re_password:
            raise serializers.ValidationError({"password": "Passwords don't match"})

        try:
            validate_password(password)
        except ValidationError as err:
            raise serializers.ValidationError({"password": err.messages})

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('re_password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
