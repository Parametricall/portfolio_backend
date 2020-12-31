from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class UsersSerializer(serializers.ModelSerializer):
    """Serializer for the User object"""

    password = serializers.CharField(
        write_only=True,
        required=False
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = "__all__"

    def create(self, validated_data):
        """
        Create new User profile.

        Required to call "set_password" to encrypt password.
        """
        user = get_user_model()(
            **validated_data,
        )

        password = validated_data.get("password", None)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save()
        return user

    def validate(self, data):
        password = data.get("password", None)
        confirm_password = data.get("confirm_password", None)
        if password:
            if password == confirm_password:
                del data["confirm_password"]
            else:
                raise serializers.ValidationError("Those passwords don't "
                                                  "match.")

        return data


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return attrs
