from .models import Resume
from .serializers import ResumeSerializer
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

# 이력서 페이지네이션
class SetPagination(PageNumberPagination):
  page_size = 8
  page_query_param = 'page_size'
  max_page_size = 100
  
class ResumeViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
      user = self.request.user
      if user.is_authenticated:
        return Resume.objects.filter(user=user)
      else:
        return Resume.objects.none()
    serializer_class = ResumeSerializer
    pagination_class = SetPagination
    filter_backends = [SearchFilter]
    search_fields=('title',)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#Filtering 포트폴리오에서 자신이 작성한 글 조회
#Request 보낸 유저가 등록이 되어 있다면, 해당 유저가 작성한 글만 필터링해서 response 해준다. 
#Request 보낸 유저가 등록이 안 되어 있다면, 빈 리스트를 response 해준다. 
class ResumeList(generics.ListAPIView):

    serializer_class = ResumeSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Resume.objects.filter(resume=user)
        else:
            return Resume.objects.none()
