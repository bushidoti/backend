from django.urls import path

from .views import  DocumentApiRetrieve

urlpatterns = [
    path('documents/', DocumentApiRetrieve.as_view()),
]
