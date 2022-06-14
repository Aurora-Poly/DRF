from .models import Resume
from .serializers import ResumeSerializer
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    filter_backends = [SearchFilter]
    search_fields=('title',)


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
