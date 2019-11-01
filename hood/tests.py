from django.test import TestCase
from .models import Business, Neighborhood
# Create your tests here.


class NeighborhoodTest(TestCase):
    def setUp(self):
        self.name = Neighborhood(name = 'runda', location = 'Nairobi')


    def test_instance(self):
        self.assertTrue(isinstance(self.runda,Neighborhood))


    def test_save_method(self):
        self.runda.save_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(Neighborhood) > 0)


class BusinessTest(TestCase):
    def setUp(self):
        self.name = Neighborhood(name = 'shop', neighborhood = 'runda', user = 'jane'), 


    def test_instance(self):
        self.assertTrue(isinstance(self.shop,Business))


    def test_save_method(self):
        self.shop.save_business()
        businessess = Business.objects.all()
        self.assertTrue(len(Business) > 0)