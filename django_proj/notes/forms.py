from django import forms
from .models import Note

class NoteForm(forms.ModelForm):

    title = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)
    topic = forms.CharField(widget=forms.Textarea)
    

    class Meta:
        model = Note
        fields = ['title', 'content', 'topic', 'created_by']