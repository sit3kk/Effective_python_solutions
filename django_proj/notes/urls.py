

from django.urls import path
from .views import NoteCreateView, NoteUpdateView, NoteDeleteView, NoteListView, NoteDetailView
from . import views

urlpatterns = [



    path('create/', NoteCreateView.as_view(), name='create_note'),
    path('', NoteListView.as_view(), name='notes_list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/update/', NoteUpdateView.as_view(), name='update_note'),
    path('<int:pk>/delete/', NoteDeleteView.as_view(), name='delete_note'),


]