from django.conf import settings
from django.shortcuts import render


# Create your views here.
def robotstxt(request):
    if settings.DEBUG:
        return render(request, 'djrobots/robots-debug.txt', content_type='text/plain')
    else:
        return render(request, 'djrobots/robots.txt', content_type='text/plain')