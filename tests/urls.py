from django.conf.urls import url, include

def dummy_sitemap(request):
    from django.http import HttpResponse
    return HttpResponse("Here's the text of the Web page.")

urlpatterns = [
    url(r'^robots\.txt$', include('djrobots.urls')),
    url(r'^sitemap\.xml$', dummy_sitemap, name='sitemap')
]
