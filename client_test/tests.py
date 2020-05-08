from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import Client

# Create your tests here.
class IndexViewTestCase(TestCase):
    USERNAME='testuser123'
    PASSWORD='P@ssw0rd'

    def setUp(self):
        # Create a new user for this unit test
        User.objects.create_user(username=self.USERNAME, password=self.PASSWORD)

    def tearDown(self):
        # Remove the test user
        user = User.objects.get(username=self.USERNAME)
        user.delete()
    
    def test_index_view(self):
        """Validated the the index view returns successfully and what we expect"""
        task_id = 75
        url = reverse('client_test:ctv-index', kwargs={'task_id': task_id})
        self.assertEqual(url, f'/demo/{task_id}/')

        client = Client()
        login_status = client.login(username=self.USERNAME, password=self.PASSWORD)
        self.assertTrue(login_status)

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response.content, f'task id is {task_id}')

