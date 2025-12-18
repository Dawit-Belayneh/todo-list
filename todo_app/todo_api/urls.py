from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view(), name='signup'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('todos/', views.TodoItemListCreateAPIView.as_view(), name='todoitem-list-create'),
    path('todos/<int:pk>/', views.TodoItemRetrieveUpdateDestroyAPIView.as_view(), name='todoitem-detail'),
]
