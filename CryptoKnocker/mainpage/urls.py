__author__ = 'trs'

from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^$", "mainpage.views.index"),
)
