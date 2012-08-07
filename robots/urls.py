from django.conf.urls import patterns, url
from .views import robots_txt


urlpatterns = patterns('',
    url(r'^$', robots_txt, name='robots_txt'),
)
