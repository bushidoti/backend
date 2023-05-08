from django.urls import path

from .views import DocumentApiRetrieve

urlpatterns = [
    path('documents/<pk>', DocumentApiRetrieve.as_view()),
]
