from django.urls import path
from . import views

urlpatterns = [
    path('', views.kanban_list, name='kanban-list'),
    path('<str:kanban_name>/', views.kanban_detail, name='kanban-detail'),
]
