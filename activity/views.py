
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    filter_backends = [SearchFilter]
    search_fields=('name', 'tag', 'company', 'field', 'detail',)