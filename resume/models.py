from django.db import models

# Create your models here.
from account.models import User


class Resume(models.Model):
  id = models.AutoField(primary_key=True, null=False, blank=False)
  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='resume')

  title = models.CharField(max_length=100) #제목
  file_upload = models.FileField(upload_to='mypage/resume/files/%Y/%m/%d', blank=True) #파일
  date = models.DateField() #날짜
  comments = models.TextField(max_length=500) #코멘트
  
