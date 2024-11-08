from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee

class EmployeeTests(APITestCase):

    def test_create_employee(self):
        url = reverse('employee-list')
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees(self):
        url = reverse('employee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        employee = Employee.objects.create(name='Jane Doe', email='jane@example.com')
        url = reverse('employee-detail', args=[employee.id])
        data = {'name': 'Jane Smith'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        employee = Employee.objects.create(name='Jane Doe', email='jane@example.com')
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
