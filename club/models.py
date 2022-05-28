from django.db import models
from django.conf import settings

class Club(models.Model):
  title = models.CharField(max_length=100)
  name = models.CharField(max_length=30)
  personnel = models.IntegerField()
  content = models.TextField()
  date = models.DateField()

  def __str__(self):
    return f'[{self.pk}]{self.title}by{self.name}'
