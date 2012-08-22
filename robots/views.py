from django.template.response import TemplateResponse
from sitesutils.helpers import get_site_id
from .models import File


def robots_txt(request):
    site_id = get_site_id(request)
    try:
        file = File.objects.get(site_id=site_id)
    except File.DoesNotExist:
        file = None
    return TemplateResponse(request, 'robots/robots.txt', {
        'object': file,
    }, content_type='text/plain')
