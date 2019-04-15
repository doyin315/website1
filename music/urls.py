from django.conf.urls import url
from . import views

app_name='music'

urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'),
    url('^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url('album/add/$',views.AlbumCreate.as_view(), name='album-add'),
    url('album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),
    url('album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),


]
