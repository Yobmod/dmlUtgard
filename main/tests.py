from django.test import TestCase
import pytest
import os
import dotenv
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


def test_env() -> None:
	try:
		dotenv.read_dotenv('.env')
	except UserWarning:
		pass
	else:
		LOCAL = os.environ['LOCAL']
		assert isinstance(LOCAL, str) and len(LOCAL) > 1 and (LOCAL == "yes" or LOCAL == "no")
