from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
                "id", "email", "first_name", "last_name",
                "password", "phone_number", "sex"
                )
        extra_kwargs = {
            'phone_number': {'required': True},
            'sex': {'required': True}
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes user data."""

    class Meta:
        model = User
        fields = ('url', 'email')
