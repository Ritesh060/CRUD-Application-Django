from django.urls import path, include
from . import views
urlpatterns = [
    path('teams/', views.TeamIndexView.as_view(), name='index'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('team/', views.teamview, name='team'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('users/', views.UserIndexView.as_view(), name='index1'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='detail1'),
    path('edit1/<int:pk>/', views.edit1, name='edit1'),
    path('user/', views.userview, name='user'),
    path('delete1/<int:pk>/', views.delete1, name='delete1'),
    path('login/', views.user_login, name='login'),
    path('home/', views.links, name='links'),
    path('', views.home, name = 'home'),
]