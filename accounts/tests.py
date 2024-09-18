from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, InvestmentAccount, Transaction

class InvestmentAccountTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_investment_account(self):
        response = self.client.post('/api/investment-accounts/', {'name': 'Test Account'})
        self.assertEqual(response.status_code, 201)
