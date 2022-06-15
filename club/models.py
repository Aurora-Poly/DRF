from django.db import models
from django.conf import settings

from account.models import User


class Club(models.Model):

  id = models.AutoField(primary_key=True, null=False, blank=False)
  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='club')

  title = models.CharField(max_length=100)
  name = models.CharField(max_length=30)
  personnel = models.IntegerField()
  content = models.TextField()
  date = models.DateField()

  def __str__(self):
    return f'[{self.pk}]{self.title}by{self.name}'
