from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('permission/', views.PermissionView.as_view(), name='permission'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
