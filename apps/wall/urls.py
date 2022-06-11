from django.conf.urls import url
from . import views  

urlpatterns = [
    url(r'^$', views.index),
    url(r'new/message$', views.new_message),
    url(r'new/comment$', views.new_comment),
    url(r'destroy/message/(?P<num>\d+)$', views.destroy_message),
    url(r'like/message/(?P<num>\d+)$', views.like_message),
    url(r'like/comment/(?P<num>\d+)$', views.like_comment),
    url(r'unlike/(?P<num>\d+)$', views.dislike),
    url(r'unlike-c/(?P<num>\d+)$', views.dislike_c),
    url(r'destroy/comment/(?P<num>\d+)$', views.destroy_comment),
    url(r'logout$', views.logout),
]