from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"), # First path is to create a new notes and this is goning to views.NoteListCreate.as_view()
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"), # Second path is notes/delete and this <int:pk> the primary key that will be deleted
]