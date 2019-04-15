from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('admin/', admin.site.urls),
    url('music/', include('music.urls')),
]

