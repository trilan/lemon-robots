from django.template.response import TemplateResponse

from .models import File
from .utils import get_site_id


def robots_txt(request):
    site_id = get_site_id(request)
    try:
        file = File.objects.get(site_id=site_id)
    except File.DoesNotExist:
        file = None
    return TemplateResponse(request, 'robots/robots.txt', {
        'object': file,
    }, content_type='text/plain')
