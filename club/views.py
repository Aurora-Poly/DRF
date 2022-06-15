from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Club
from .permissions import IsOwnerOrReadOnly
from .serializers import ClubSerializer
from rest_framework import viewsets
class SetPagination(PageNumberPagination):
  page_size = 3
  page_query_param = 'page_size'
  max_page_size = 100
# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    pagination_class = SetPagination
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
      serializer.save(user=self.request.user)