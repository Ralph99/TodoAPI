from django.test import TestCase

# Create your tests here.
from rest_framework.test import APIRequestFactory

#   post request test
factory = APIRequestFactory()
request = factory.post('api/', {'name': 'do the dishes', 'body': 'quickly o the dishes before moving onto the next thing'})
