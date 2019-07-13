from django.urls import path
from profiles_api import views

urlpatterns = [
    path('helloworld/', views.HelloApiView.as_view()),
]
