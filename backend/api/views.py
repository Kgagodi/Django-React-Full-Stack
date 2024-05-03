from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class NoteListCreate(generics.ListCreateAPIView):  ## ANY DATA THAT IS REQUIRED TO CREATE A NEW NOTES IT WILL BE ACCEPTED AND BE PARSED TO Class UserSerializer to check if the data is accurate according to the fields requirements e.g Date, TextField length, etc
   serializer_class = NoteSerializer
   permission_classes = [IsAuthenticated] # to authorise the user to access the class

   def get_queryset(self):
        user = self.request.user # to give us user object if you are authonticated for that specific class
        return Note.objects.filter(author=user) # To filter the notes writen by a specific user filtering infor using the author=user.  To filter all the notes we write [ Note.objects.all]

   def perform_create(self, serializer): # Customise configuiration to create a new user by accessing the Serializer.py by serializer to check the does  not exists so that it can add a new user, otherwise it will give error if the user is valid
        if serializer.is_valid(): # When parsing a data (NoteSerializer) it will validate it
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer 
    permission_classes = [IsAuthenticated] # to authorise the user to access the class

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user) # Here we specify the Note or user that we want to delete if we are authonticated



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
