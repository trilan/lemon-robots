from django.contrib import admin as django_admin
from django.test import TestCase

from lemon import extradmin as lemon_admin
from lemon.extradmin import ModelAdmin

from robots.admin import FileAdmin
from robots.models import File


class FileAdminTests(TestCase):

    def test_class(self):
        self.assertTrue(issubclass(FileAdmin, ModelAdmin))


class AdminSiteTests(TestCase):

    def test_file_isnt_registered_in_django(self):
        self.assertNotIn(File, django_admin.site._registry)

    def test_file_is_registered_in_lemon(self):
        self.assertIsInstance(lemon_admin.site._registry[File], FileAdmin)
