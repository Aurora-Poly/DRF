from django.urls import path, include
from .views import ContestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('contest', ContestViewSet)

urlpatterns =[
    path('', include(router.urls))
]