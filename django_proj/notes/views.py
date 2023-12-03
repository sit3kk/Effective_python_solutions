from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Note
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
         if self.request.user.is_superuser:
            return Note.objects.all()
         else:
            return Note.objects.filter(created_by=self.request.user)


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'notes/create_note.html'
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'notes/update_note.html'
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        note = self.get_object()
        return self.request.user == note.created_by

class NoteDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = '/notes/'

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(created_by=owner)
    
    def test_func(self):
        note = self.get_object()
        return self.request.user == note.created_by or self.request.user.is_superuser


def home(request):

    return render(request, 'notes/home.html')



def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.info(request, 'Username does not exist')
            return render(request, 'notes/login_register.html')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'notes/login_register.html')


    context = {}

    return render(request, 'notes/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            try:
                user = User.objects.get(username=username)
                messages.info(request, 'Username already exists')
                return render(request, 'notes/login_register.html')
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, 'User created')
                return render(request, 'notes/login_register.html')
    
        context = {}
    
        return render(request, 'notes/login_register.html', context)

