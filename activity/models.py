from django.db import models

# Create your models here.

class Activity(models.Model):
  id = models.AutoField(primary_key=True, null=False, blank=False)
  name = models.CharField(max_length=300, blank=False, null=False)
  tag = models.TextField(max_length=300, blank=False, null=False)
  company = models.TextField(max_length=100, blank=False, null=False)
  apply_period = models.DateField()
  field = models.CharField(max_length=300, blank=False, null=False)
  actperiod = models.DateField()
  personnel = models.IntegerField()
  detail=models.TextField(max_length=1000, blank=False, null=False)
  apply_url = models.CharField(max_length=300,blank=False, null=False)
  img_url = models.ImageField(upload_to=None, height_field=None, width_field=None)
#대외활동 이름 name
#관련태그 tag
#주최주관 company
#지원기간 applyperiod
#모집분야 field
#활동기간 actperiod
#모집인원 personnel
#상세설명 detail
#지원url apply-url
#이미지url img-url

class Meta:
  managed = True
  db_table = 'contest'