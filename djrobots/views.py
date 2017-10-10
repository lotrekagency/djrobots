from django.conf import settings
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def robotstxt(request):
    sitemap_view_name = getattr(settings, "DJROBOTS_SITEMAP_VIEW_NAME", None)
    sitemap_url = None
    if sitemap_view_name:
        sitemap_url = reverse(sitemap_view_name)

    if settings.DEBUG:
        return render(request, 'djrobots/robots-debug.txt', content_type='text/plain')
    else:
        return render(request, 'djrobots/robots.txt', content_type='text/plain')