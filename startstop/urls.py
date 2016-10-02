from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list_EC2_instances, name='list_EC2_instances'),
    url(r'^start_instance/$', views.start_instance, name='start_instance'),
]
