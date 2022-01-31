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

    #/town endpoint (GET)
    def test_get_town(self):
        response = self.client.get("/api/town/", {})
        self.assertEqual(response.status_code, 200, "The user should be able to access this endpoint.")

    #/town endpoint good format (GET)
    def test_get_town_good_format(self):
        response = self.client.get('/api/town/?fields=["name","code"]', {})
        self.assertEqual(response.status_code, 200, "The user should be able to access this endpoint.")

    #/town endpoint wrong format (GET)
    def test_get_town_wrong_format(self):
        response = self.client.get('/api/town/?fields=[name,code]', {})
        self.assertEqual(response.status_code, 400, "The user should get a wrong format exception.")

    #/town endpoint field not found  (GET)
    def test_get_town_wrong_field(self):
        response = self.client.get('/api/town/?fields=["names","code"]', {})
        self.assertEqual(response.status_code, 400, "The user should get a wrong format exception.")


