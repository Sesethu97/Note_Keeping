from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Note
from .serialisers import NoteSerialiser, AccountSettingsFormSerializer, UserUpdateSerialiser
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated




class HomeAPIView(APIView):
    def get(self, request):
        notes = Note.objects.all() 
        serialiser  = NoteSerialiser(notes, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)

class RegisterAPIView(APIView):
    def post(self, request: Request, *args, **kwargs):
        """
        Handles post request
        """
        if self.request.user.is_authenticated:
            data = {"status_code": 403, "message": "You are already have an account"}
            return Response(data=data, status=status.HTTP_403_FORBIDDEN)

        serialiser = AccountSettingsFormSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()

            username: str = serialiser.data.get("username")
            token: str = self.login_user_after_register(username)
            data = {
                "token": token,
                "status_code": 201,
                "message": "Successfully created your account",
            }
            return Response(data=data, status=status.HTTP_201_CREATED)



class SettingsAPIView(APIView):



    queryset = User.objects.all()
    serializer_class = UserUpdateSerialiser
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = User.objects.get(object_id=request.user.object_id)
        serialiser: UserUpdateSerialiser = self.get_serializer(
            instance, data=request.data, partial=True
        )

        if serialiser.is_valid():
            serialiser.save()
            return Response({"message": "Account Updated Successfully"})

        else:
            return Response({"message": "failed", "details": serialiser.errors})




