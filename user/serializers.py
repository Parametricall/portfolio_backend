from django.contrib.auth import get_user_model
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for the User object"""

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]

    def create(self, validated_data):
        """
        Create new User profile.

        Required to call "set_password" to encrypt password.
        """
        user = get_user_model()(
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ListUsersSerializer(serializers.ModelSerializer):
    """Serializer for the User object"""

    password = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = "__all__"
