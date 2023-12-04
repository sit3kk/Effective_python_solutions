from topics.views import TopicListView, TopicCreate, TopicUpdate, TopicDelete, TopicDetailView
from django.urls import path

urlpatterns = [
    path('', TopicListView.as_view(), name='topic-list'),
    path('create/', TopicCreate.as_view(), name='topic-create'),
    path('<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    path('<int:pk>/update/', TopicUpdate.as_view(), name='topic-update'),
    path('<int:pk>/delete/', TopicDelete.as_view(), name='topic-delete'),

]
