from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from .models import Contest
from .serializers import ContestSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer
    #SearchFilter 기반 검색
    filter_backends = [SearchFilter]
    search_fields=('name','tag', 'company', 'detail', 'qualification', 'award', 'field',)
