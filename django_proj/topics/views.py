from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from notes.models import Note
from topics.models import Topic

from django.http import Http404


class TopicListView(ListView):
    model = Topic
    template_name = 'topics/topic_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Topic.objects.all()
        else:
            return Topic.objects.filter(is_public=True)


class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topics/topic_detail.html'


    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(topic=self.get_object().pk)
        return context
    
    def get_object(self, queryset=None):
        topic = super(TopicDetailView, self).get_object(queryset)
        if topic.is_public or self.request.user.is_superuser:
            return topic
        else:
            raise Http404("No topic found matching the query")

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(topic=self.get_object().pk)
        return context


class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'parent', 'is_public']
    success_url = reverse_lazy('topic-list')
    template_name = 'topics/topic_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TopicCreate, self).form_valid(form)


class TopicUpdate(UserPassesTestMixin, UpdateView):
    model = Topic
    fields = ['title', 'parent', 'is_public']
    template_name = 'topics/topic_form.html' 
    success_url = reverse_lazy('topic-list')

    def test_func(self):
        return self.request.user == self.get_object().created_by


class TopicDelete(UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = reverse_lazy('topic-list')
    template_name = 'topics/topic_confirm_delete.html'
    success_url = reverse_lazy('topic-list')

    def test_func(self):
        return self.request.is_superuser or self.request.user == self.object.created_by