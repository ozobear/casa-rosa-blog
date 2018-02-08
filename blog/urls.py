from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
	re_path(r'^$', views.post_list_view, name='post_list_view'),
	re_path(r'^(?P<pk>[0-9]+)/$', views.post_detail_view, name='post_detail_view'),
]