from django.urls import path
from .views import ListCreateNoteView, RetrieveUpdateDestroyNoteView

urlpatterns = [
    path("", ListCreateNoteView.as_view()),
    path("<int:pk>/", RetrieveUpdateDestroyNoteView.as_view())
]