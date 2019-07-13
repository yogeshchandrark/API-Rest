from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('helloViewset', views.HellowViewSet, base_name='helloViewset')

urlpatterns = [
    path('helloworld/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
