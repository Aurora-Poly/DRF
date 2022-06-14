from .models import Portfolio
from .serializers import PortfolioSerializer
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    #SearchFilter 기반으로 검색할 예정
    #url에 "portfolio/?search=안녕" 으로 api 확인
    filter_backends = [SearchFilter]
    search_fields=('title','content',)


#Filtering 포트폴리오에서 자신이 작성한 글 조회
#Request 보낸 유저가 등록이 되어 있다면, 해당 유저가 작성한 글만 필터링해서 response 해준다. 
#Request 보낸 유저가 등록이 안 되어 있다면, 빈 리스트를 response 해준다. 
class PortfolioList(generics.ListAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Portfolio.objects.filter(portfolio=user)
        else:
            return Portfolio.objects.none()

