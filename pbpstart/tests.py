# rest_api_app/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import File
from .serializers import FileSerializer

class FileModelTest(TestCase):
    def setUp(self):
        self.file = File.objects.create(
            first_name='John',
            last_name='Doe',
            national_id='1234',
            birth_date='2000-01-01',
            address='123 Main St.',
            country='USA',
            phone_number='555-5555',
            email='johndoe@example.com',
            finger_print_signature='abc123'
        )
    
    def test_file_str(self):
        self.assertEqual(str(self.file), 'John Doe (1234)')

class FileViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.file_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'national_id': '1234',
            'birth_date': '2000-01-01',
            'address': '123 Main St.',
            'country': 'USA',
            'phone_number': '555-5555',
            'email': 'johndoe@example.com',
            'finger_print_signature': 'abc123'
        }
    
    def test_create_file(self):
        response = self.client.post(reverse('file-list'), data=self.file_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 1)
        self.assertEqual(File.objects.get().first_name, 'John')
    
    def test_create_file_missing_field(self):
        self.file_data['first_name'] = ''
        response = self.client.post(reverse('file-list'), data=self.file_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(File.objects.count(), 0)

class UserListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.file1 = File.objects.create(
            first_name='John',
            last_name='Doe',
            national_id='1234',
            birth_date='2000-01-01',
            address='123 Main St.',
            country='USA',
            phone_number='555-5555',
            email='johndoe@example.com',
            finger_print_signature='abc123'
        )
        self.file2 = File.objects.create(
            first_name='Jane',
            last_name='Doe',
            national_id='5678',
            birth_date='2000-01-02',
            address='456 Elm St.',
            country='USA',
            phone_number='555-5556',
            email='janedoe@example.com',
            finger_print_signature='def456'
        )
    
    def test_search_by_first_name(self):
        response = self.client.get(reverse('user-list'), {'search': 'John'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['first_name'], 'John')
    
    def test_search_by_last_name(self):
        response = self.client.get(reverse('user-list'), {'search': 'Doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_search_by_birth_date_range(self):
        response = self.client.get(reverse('user-list'), {'birth_date_after': '2000-01-01', 'birth_date_before': '2000-01-02'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_search_by_phone_number(self):
        response = self.client.get(reverse('user-list'), {'search': '555'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_search_by_email(self):
        response = self.client.get(reverse('user-list'), {'search': 'janedoe@example.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
    
    def test_sort_by_first_name(self):
        response = self.client.get(reverse('user-list'), {'ordering': 'first_name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['first_name'], 'Jane')
    
    def test_sort_by_last_name(self):
        response = self.client.get(reverse('user-list'), {'ordering': 'last_name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['last_name'], 'Doe')

           
