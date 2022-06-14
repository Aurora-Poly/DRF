from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from .models import Contest
from .serializers import ContestSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
class SetPagination(PageNumberPagination):
  page_size = 3
  page_query_param = 'page_size'
  max_page_size = 100
# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    pagination_class = SetPagination
    #SearchFilter 기반 검색
    filter_backends = [SearchFilter]
    search_fields=('name','tag', 'company', 'detail', 'qualification', 'award', 'field',)
