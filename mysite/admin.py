from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Msg)
class MsgAdmin(admin.ModelAdmin):
    list_display = ['mapKey', 'mapValue']
