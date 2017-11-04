from django.conf import settings
from django.shortcuts import render
from django.urls import reverse


def robotstxt(request):
    sitemaps = getattr(settings, "DJROBOTS_SITEMAPS", [])

    if isinstance(sitemaps, str):
        sitemaps = [sitemaps]
    context = {
        'sitemap_urls' : []
    }
    for sitemap in sitemaps:
        try:
            context['sitemap_urls'].append(reverse(sitemap))
        except:
            context['sitemap_urls'].append(sitemap)

    if settings.DEBUG:
        return render(request, 'djrobots/robots-debug.txt', context, content_type='text/plain')
    else:
        return render(request, 'djrobots/robots.txt', context, content_type='text/plain')