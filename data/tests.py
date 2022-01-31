from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
#Test Town
class TownTestCase(TestCase):
    fixtures = ['data.json']

    #setUp for login
    def setUp(self):
        self.client = Client()
        self.username = 'userTest'
        self.email = 'test@test.com'
        self.password = 'C}n$A2\khS4"}SM'        
        self.test_user = User.objects.create_superuser(self.username, self.email, self.password)
        self.client.login(username=self.username, password=self.password)

    #Step 1 tests :
    #/town endpoint (GET)
    def test_get_town(self):
        response = self.client.get("/api/town/", {})
        self.assertEqual(response.status_code, 200, "The user should be able to access this endpoint.")

    #/town endpoint good format (GET)
    def test_get_town_good_format(self):
        response = self.client.get('/api/town/?fields=["name","population"]', {})
        self.assertEqual(response.status_code, 200, "The user should be able to access this endpoint.")

    #/town endpoint wrong format (GET)
    def test_get_town_wrong_format(self):
        response = self.client.get('/api/town/?fields=[name,population]', {})
        self.assertEqual(response.status_code, 400, "The user should get a wrong format exception.")

    #/town endpoint field not found  (GET)
    def test_get_town_wrong_field(self):
        response = self.client.get('/api/town/?fields=["names","population"]', {})
        self.assertEqual(response.status_code, 400, "The user should get a wrong format exception.")

    #Step 2 tests :
    #/town filter endpoint good format (GET)
    def test_get_town_filter_good_format(self):
        response = self.client.get('/api/town/?fields=["name","population"]&filters={"field":"name","value": "Paris","predicate": "contains"}', {})
        self.assertEqual(response.status_code, 200, "The user should be able to access this endpoint.")

    #/town filter endpoint wrong format (GET)
    def test_get_town_filter_wrong_format(self):
        response = self.client.get('/api/town/?fields=["name","population"]&filters={"field""name","value": "Paris","predicate": "contains"}', {})
        self.assertEqual(response.status_code, 400, "The user should get a wrong format exception.")
    
    #/town filter endpoint missing field (GET)
    def test_get_town_filter_missing_field(self):
        response = self.client.get('/api/town/?fields=["name","population"]&filters={"field":"names","value": "Paris","predicate": "contains"}', {})
        self.assertEqual(response.status_code, 400, "The user should get a missing field exception.")

    #/town filter endpoint field not found (GET)
    def test_get_town_filter_wrong_field(self):
        response = self.client.get('/api/town/?fields=["names","population"]&filters={"field":"name","value": "Paris","predicate": "contains"}', {})
        self.assertEqual(response.status_code, 400, "The user should get a field not found exception.")
    
    #/town filter endpoint wrong value type (GET)
    def test_get_town_filter_wrong_type(self):
        response = self.client.get('/api/town/?fields=["name","population"]&filters={"field":"code","value": "Paris","predicate": "eq"}', {})
        self.assertEqual(response.status_code, 400, "The user should get a wrong value type exception.")
    
    #/town filter endpoint no result found (GET)
    def test_get_town_filter_notFound(self):
        response = self.client.get('/api/town/?fields=["name","population"]&filters={"field":"name","value": "Marseille","predicate": "eq"}', {})
        self.assertEqual(response.status_code, 404, "The user should get a not found exception.")
