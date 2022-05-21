from .models import Portfolio
from .serializers import PortfolioSerializer
from rest_framework import viewsets

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer