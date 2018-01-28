from django.test import TestCase, Client
import pytest
import os
from dmlutgard.settings import *
from dmlutgard.urls import *
import warnings
warnings.filterwarnings("error")


class MainViewsTestCase(TestCase):
	def test_homepage(self) -> None:
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_facilities(self) -> None:
		resp = self.client.get('/facilities/')
		self.assertEqual(resp.status_code, 200)

	def test_projects(self) -> None:
		resp = self.client.get('/projects/')
		self.assertEqual(resp.status_code, 200)

	def test_publications(self) -> None:
		resp = self.client.get('/publications/')
		self.assertEqual(resp.status_code, 200)

	def test_fakeUrl(self) -> None:
		resp = self.client.get('/fakeUrl/')
		self.assertEqual(resp.status_code, 404)

	def test_admin(self) -> None:
		resp = self.client.get('/admin/login/?next=/admin/')
		self.assertEqual(resp.status_code, 200)

	# def test_an_admin_view(self):
	# 	admin_client = Client()
	# 	response = admin_client.get('/admin/')
	# 	assert response.status_code == 200

	def test_admin_doc(self) -> None:
		resp = self.client.get('/admin/login/?next=/admin/doc/')
		self.assertEqual(resp.status_code, 200)


def test_URLS() -> None:
	assert isinstance(urlpatterns, list) and len(urlpatterns) >= 1


def test_LOCAL() -> None:
	assert isinstance(LOCAL, str) and len(LOCAL) > 1 and (LOCAL == "yes" or LOCAL == "no")


def test_EMAIL_HOST() -> None:
	assert isinstance(EMAIL_HOST_USER, str) and len(EMAIL_HOST_USER) > 1
	assert isinstance(EMAIL_HOST_PASSWORD, str) and len(EMAIL_HOST_PASSWORD) > 1
