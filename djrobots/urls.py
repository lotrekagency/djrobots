from django.urls import re_path

from djrobots.views import robotstxt

urlpatterns = [
    re_path(r'^$', robotstxt, name='djrobots'),
]
