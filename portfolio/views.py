from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Portfolio
from .permissions import IsOwner
from .serializers import PortfolioSerializer
from rest_framework import viewsets, generics, filters
from rest_framework.filters import SearchFilter
class SetPagination(PageNumberPagination):
  page_size = 8
  page_query_param = 'page_size'
  max_page_size = 100
# class PortfolioList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated, IsOwner]
#       pagination_class = SetPagination
#     def get_queryset(self):
#       user = self.request.user
#       if user.is_authenticated:
#         return Portfolio.objects.filter(user=user)
#       else:
#         return Portfolio.objects.none()
#     #queryset = Portfolio.objects.filter(user=1)
#     serializer_class = PortfolioSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields=['title','content']
#     def perform_create(self, serializer):
#       serializer.save(user=self.request.user)
#
# # Blog의 detail을 보여주는 역할
# class PortfolioDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated, IsOwner]
#     queryset = Portfolio.objects.all()
#     serializer_class = PortfolioSerializer


# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class PortfolioViewSet(viewsets.ModelViewSet):
    #queryset = Portfolio.objects.all()
    def get_queryset(self):
      user = self.request.user
      if user.is_authenticated:
        return Portfolio.objects.filter(user=user)
      else:
        return Portfolio.objects.none()

    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    pagination_class = SetPagination



    #SearchFilter 기반으로 검색할 예정
    #url에 "portfolio/?search=안녕" 으로 api 확인
    filter_backends = [SearchFilter]
    search_fields=('title','content',)
    #url에 "portfolio/? search=안녕" 으로 api 확인
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields=['title','content']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#Filtering 포트폴리오에서 자신이 작성한 글 조회
#Request 보낸 유저가 등록이 되어 있다면, 해당 유저가 작성한 글만 필터링해서 response 해준다.
#Request 보낸 유저가 등록이 안 되어 있다면, 빈 리스트를 response 해준다.
class PortfolioList(generics.ListAPIView):
    serializer_class = PortfolioSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Portfolio.objects.filter(user=user)
        else:
            return Portfolio.objects.none()

