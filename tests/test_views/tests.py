from django.contrib.sites.models import Site
from django.test import TestCase, RequestFactory

from robots.models import File
from robots.views import robots_txt


class RobotsTxtViewTests(TestCase):

    def setUp(self):
        self.site1 = Site.objects.get(id=1)
        self.site2 = Site.objects.create(
            domain='s2.example.com',
            name='s2.example.com',
        )
        self.file = File.objects.create(site=self.site1)

    def get_request(self, site=None):
        request_factory = RequestFactory()
        request = request_factory.get('/robots.txt')
        if site is not None:
            request.site = site
        return request

    def test_has_file_object_in_context_if_exists(self):
        response = robots_txt(self.get_request(self.site1))
        self.assertEqual(response.context_data['object'], self.file)

    def test_has_none_in_context_if_file_doesnt_exist(self):
        response = robots_txt(self.get_request(self.site2))
        self.assertIsNone(response.context_data['object'])
