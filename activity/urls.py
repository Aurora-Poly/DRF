from django.urls import path, include
from .views import ActivityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('activity', ActivityViewSet)

urlpatterns =[
    path('', include(router.urls))
]