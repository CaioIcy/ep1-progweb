from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='absentpi-index'),
    url(r'^show/(?P<entry_id>\d+)/$', views.show, name='absentpi-show'),
]
