from django.test import TestCase

class MainViewsTestCase(TestCase):
	def test_homepage(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)
