from django.conf.urls import url

from djrobots.views import robotstxt

urlpatterns = [
    url(r'^$', robotstxt, name='djrobots'),
]