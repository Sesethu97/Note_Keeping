from rest_framework import serializers
from notes.models import Note
from django.contrib.auth.models import User

class NoteSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "description", "draft", "saved"]

class AccountSettingsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email", "password"]

    def create(cls, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class NoteUpdateFormSerializer(serializers.ModelSerializer):
     class Meta:
        model = Note
        fields = ["title", "description", "draft", "saved"]


class UserUpdateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
        )