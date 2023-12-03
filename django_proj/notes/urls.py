

from django.urls import path
from .views import NoteCreateView, NoteUpdateView, NoteDeleteView, NoteListView, NoteDetailView
from . import views

urlpatterns = [



    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('', views.home, name='home' ),
    path('create/', NoteCreateView.as_view(), name='create_note'),
    path('notes/', NoteListView.as_view(), name='notes_list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='update_note'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='delete_note'),


]