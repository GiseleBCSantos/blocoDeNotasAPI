from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

class ListCreateNoteView(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class RetrieveUpdateDestroyNoteView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
