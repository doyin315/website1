from django.conf.urls import url
from . import views

app_name='music'

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    url('^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),

]
