from django.db import models


# Create your models here.
class Msg(models.Model):
    mapKey = models.TextField(blank=True, verbose_name='MAP_KEY')
    mapValue = models.TextField(blank=True, verbose_name='MAP_VALUE')
