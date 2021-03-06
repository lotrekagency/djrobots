from django.conf import settings
from django.shortcuts import render
from django.urls import reverse


def robotstxt(request):
    sitemaps = getattr(settings, "DJROBOTS_SITEMAPS", [])
    disallow_all = getattr(settings, "DJROBOTS_DISALLOWALL", False)

    if isinstance(sitemaps, str):
        sitemaps = [sitemaps]

    context = {
        'sitemap_urls': []
    }
    for sitemap in sitemaps:
        try:
            context['sitemap_urls'].append(
                request.build_absolute_uri(
                    reverse(sitemap)
                )
            )
        except: # NOQA
            context['sitemap_urls'].append(sitemap)

    if settings.DEBUG or disallow_all:
        return render(
            request, 'djrobots/robots-debug.txt',
            context, content_type='text/plain'
        )
    else:
        return render(
            request, 'djrobots/robots.txt',
            context, content_type='text/plain'
        )
