from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Note
from .serialisers import (
    NoteSerialiser,
    AccountSettingsSerializer,
    UserUpdateSerialiser,
    NoteUpdateSerializer,
    UpdateSerializer,
)
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    UpdateAPIView,
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    DestroyAPIView
    
)
from django.db import models


class HomeAPIView(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serialiser = NoteSerialiser(notes, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)


class RegisterAPIView(APIView):
    def post(self, request: Request, *args, **kwargs):
        """
        Handles post request
        """
        if self.request.user.is_authenticated:
            data = {"status_code": 403, "message": "You are already have an account"}
            return Response(data=data, status=status.HTTP_403_FORBIDDEN)

        serialiser = AccountSettingsSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()

            username: str = serialiser.data.get("username")
            data = {
                "status_code": 201,
                "message": "Successfully created your account",
            }
            return Response(data=data, status=status.HTTP_201_CREATED)


class SettingsAPIView(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserUpdateSerialiser
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = User.objects.get(object_id=request.user.object_id)
        serialiser: UserUpdateSerialiser = self.get_serializer(
            instance, data=request.data, partial=True
        )

        if serialiser.is_valid():
            serialiser.save()
            return Response({"message": "Account Updated Successfully"})

        else:
            return Response({"message": "failed", "details": serialiser.errors})


class AddAPIView(CreateAPIView):
    # queryset = Note.objects.all()
    serializer_class = NoteSerialiser

    permission_classes = [IsAuthenticated]

    def create(self, serializer: NoteSerialiser):
        user: User = self.request.user
        user.posts += 1
        user.save()
        return serializer.save(author=user)

    def create(self, request: Request, *args, **kwargs):
        serialiser = self.get_serializer(data=request.data)
        serialiser.is_valid(raise_exception=True)
        instance = self.perform_create(serialiser)
        instance_serialiser = NoteSerialiser(instance)
        return Response(instance_serialiser.data)


class DetailAPIView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteUpdateSerializer
    lookup_field = "id"


class UpdateAPIView(UpdateAPIView):
    queryset = Note.objects.all()

    serializer_class = UpdateSerializer

    def patch(self, request, *args, **kwargs):
        instance = User.objects.get(object_id=request.user.object_id)
        serialiser: UpdateSerializer = self.get_serializer(
            instance, data=request.data, partial=True
        )

        if serialiser.is_valid():
            serialiser.save()
            return Response({"message": "Note Updated Successfully"})

        else:
            return Response({"message": "failed", "details": serialiser.errors})


class DeleteAPIView(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerialiser
    lookup_field = "id"

class ImportantsAPIView(APIView):
    # queryset = Note.objects.all()
    # serializer_class = NoteSerialiser

    def post(self, request: Request, pk):
        note = Note.objects.get(id=pk)
        note.important = not note.important
        note.save()
        return Response({"yes": "done"}, status=status.HTTP_200_OK)

class ImportantListsAPIView(APIView):
    def get(self, request):
        notes = Note.objects.filter(author=request.user, important=True)
        serialiser = NoteSerialiser(notes, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)
       



class LogInAPIView(APIView):
    serializer_class = AccountSettingsSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request: Request, *args, **kwargs):
        """
        Handles post request
        """
        data = request.data
        serialiser = AccountSettingsSerializer(data=data)

        if serialiser.is_valid(raise_exception=True):
            new_data = serialiser.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

