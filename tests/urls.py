from django.urls import re_path, include

def dummy_sitemap(request):
    from django.http import HttpResponse
    return HttpResponse("Here's the text of the Web page.")

urlpatterns = [
    re_path(r'^robots\.txt$', include('djrobots.urls')),
    re_path(r'^sitemap\.xml$', dummy_sitemap, name='sitemap')
]
