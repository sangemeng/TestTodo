from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getjson', views.get_json, name='get_json'),
    path('setjson', views.set_json, name='set_json'),
]