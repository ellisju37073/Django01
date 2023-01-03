from django.urls import re_path
from games import views

urlpatterns = [
    re_path(r'^games/$', views.game_list),
    re_path(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
]