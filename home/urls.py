from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = "home"

urlpatterns = [
	path(r'', views.artist_list_view, name='artist_list_view'),
	re_path(r'^(?P<slug>[\w-]+)/$', views.artist_detail_view, name='artist_detail_view'),
]