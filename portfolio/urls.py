from django.urls import path, include
#from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import PortfolioViewSet
from rest_framework.routers import DefaultRouter
# urlpatterns =[
#     path('portfolio/', views.PortfolioList.as_view()),
#     path('portfolio/<int:pk>/', views.PortfolioDetail.as_view()),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
router = DefaultRouter()
# 첫 번째 인자는 url의 prefix
# 두 번째 인자는 ViewSet
router.register('portfolio', PortfolioViewSet, basename='portfolio')

urlpatterns =[
    path('', include(router.urls)),
]