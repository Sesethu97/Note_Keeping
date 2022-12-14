from rest_framework import serializers
from notes.models import Note
from django.contrib.auth.models import User

class NoteSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "description", "draft", "saved"]


class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email", "password"]

    def create(cls, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class NoteUpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Note
        fields = ["id", "title", "description", "draft", "saved"]


class UpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Note
        fields = ["id", "title", "description"]



class UserUpdateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
        )
    
