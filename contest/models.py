from django.db import models

class Contest(models.Model):
  name = models.CharField(max_length=300, blank=False, null=False)
  tag = models.TextField(max_length=300, blank=False, null=False)
  company = models.TextField(max_length=100, blank=False, null=False)
  detail = models.TextField(max_length=1000, blank=False, null=False)
  qualification = models.CharField(max_length=300, blank=False, null=False)
  award = models.CharField(max_length=100, blank=False, null=False)
  field = models.CharField(max_length=300, blank=False, null=False)
  apply_url = models.CharField(max_length=300,blank=False, null=False)
  img_url = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=300)
#공모전 이름 contest_name
#관련태그 tag
#주최주관 company 
#상세설명 detail
#자격요건 qualification
#시상내역 award
#공모분야 field
#지원url apply-url
#이미지url img-url
