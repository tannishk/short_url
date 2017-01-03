#__author__ = 'sudhir'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$',views.create,name='create'),
    url(r'^ab/(?P<ur>[a-zA-Z0-9]+)/$',views.re,name='re'),
    url(r'^list/$',views.list,name='list')

]
