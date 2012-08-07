from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    url(r'^robots\.txt$', include('robots.urls')),
)
