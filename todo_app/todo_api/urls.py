from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoItemListCreateAPIView.as_view(), name='todoitem-list-create'),
    path('todos/<int:pk>/', views.TodoItemRetrieveUpdateDestroyAPIView.as_view(), name='todoitem-detail'),
]
