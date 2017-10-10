from django.conf import settings
from django.shortcuts import render
from django.urls import reverse


def robotstxt(request):
    sitemap_view_name = getattr(settings, "DJROBOTS_SITEMAP_VIEW_NAME", None)
    sitemap_url = None
    context = {}
    if sitemap_view_name:
        sitemap_url = reverse(sitemap_view_name)
        context = {
            'sitemap_url' : sitemap_url
        }

    if settings.DEBUG:
        return render(request, 'djrobots/robots-debug.txt', context, content_type='text/plain')
    else:
        return render(request, 'djrobots/robots.txt', context, content_type='text/plain')