from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

# Create your tests here.
print ('11111111111111111')
User =  get_user_model()
print ('22222222222222222')
print(User)

class QuickStartTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create(username='abc', password='somepasS23')
		User.objects.create(username='xyz', password='somepasS23')

	def test_user_created(self):
		user =  User.objects.get(username='xyz')
		self.assertEqual(user.username, 'xyz')

	def test_user_delete(self):
		user = User.objects.get(username="abc")
		print(user)
		user.delete()
		print("********************")

		try:
			user = User.objects.get(username="abc")

		except:
			user =  None

		print(user)
		self.assertNotEqual(user, "abc")

		# seft.assertEqual
	def test_admin_rights(self):
		client = APIClient()
		client.login(username=self.user.username, password="somepasS23")
