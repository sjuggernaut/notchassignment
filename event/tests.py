from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from event.models import Event
from datetime import datetime


class EventTests(APITestCase):
    """
    TestCase class for Events URLs
    """

    def test_create_event(self):
        """
        Test creating an event.
        :return:
        """
        url = reverse('event-manage')
        response = self.client.post(url, {
            "email": "test62@gmail.com",
            "environment": "development",
            "component": "inventory",
            "message": "this is a error message",
            "data": {
                "order_id": "162"
            }
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)

    def test_get_event(self):
        """
        Test fetching events
        :return:
        """
        url = reverse('event-manage')
        self.client.post(url, {
            "email": "test62@gmail.com",
            "environment": "development",
            "component": "inventory",
            "message": "this is a error message",
            "data": {
                "order_id": "162"
            }
        }, format='json')
        response = self.client.get(url, {
            "message": "error",
            "email": "test62@gmail.com"
        }, format='json')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(Event.objects.count(), 1)

    def test_filter_createdAt(self):
        """
        Test filter createdat
        :return:
        """
        url = reverse('event-manage')
        self.client.post(url, {
            "email": "test-1@gmail.com",
            "environment": "development",
            "component": "inventory",
            "message": "this is an error message",
            "data": {
                "order_id": "0001"
            }
        }, format='json')
        self.client.post(url, {
            "email": "test-1@gmail.com",
            "environment": "development",
            "component": "inventory",
            "message": "this is an error message",
            "data": {
                "order_id": "0002"
            }
        }, format='json')
        self.client.post(url, {
            "email": "test-1@gmail.com",
            "environment": "development",
            "component": "inventory",
            "message": "this is a plain message",
            "data": {
                "order_id": "0003"
            }
        }, format='json')
        self.assertEqual(Event.objects.count(), 3)

        filter_date = datetime.strftime(datetime.today(), "%m-%d-%Y")
        response = self.client.get(url, {
            "email": "test-1@gmail.com",
            "message": "error",
            "createdAt": filter_date
        }, format='json')
        self.assertEqual(len(response.data), 3)
