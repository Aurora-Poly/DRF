from django.urls import path, include
from .views import ResumeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('resume', ResumeViewSet,basename='resume')

urlpatterns =[
    path('', include(router.urls))
]