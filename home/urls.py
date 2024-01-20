from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('idea/<int:pk>/', views.idea_detail, name='idea_detail'),
    path('idea/create/', views.idea_create, name='idea_create'),
    path('idea/<int:pk>/update/', views.idea_update, name='idea_update'),
    path('idea/<int:pk>/delete/', views.idea_delete, name='idea_delete'),
]