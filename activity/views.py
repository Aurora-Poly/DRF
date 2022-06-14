from rest_framework.pagination import PageNumberPagination

from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class SetPagination(PageNumberPagination):
  page_size = 10
  page_query_param = 'page_size'
  max_page_size = 100
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = SetPagination

    filter_backends = [SearchFilter]
    search_fields=('name', 'tag', 'company', 'field', 'detail',)