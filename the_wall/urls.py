from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('apps.logreg.urls')),
    url(r'wall', include('apps.wall.urls')),
    url('admin/', admin.site.urls),
]
