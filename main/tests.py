from django.test import TestCase
import pytest
import os
import dotenv

# dotenv.read_dotenv('.env')


class MainViewsTestCase(TestCase):
	def test_homepage(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_facilities(self):
		resp = self.client.get('/facilities/')
		self.assertEqual(resp.status_code, 200)

	def test_projects(self):
		resp = self.client.get('/projects/')
		self.assertEqual(resp.status_code, 200)

	def test_publications(self):
		resp = self.client.get('/publications/')
		self.assertEqual(resp.status_code, 200)

	def test_fakeUrl(self):
		resp = self.client.get('/fakeUrl/')
		self.assertEqual(resp.status_code, 404)
