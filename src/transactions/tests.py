from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Customer, Transaction, BNPLPlan
import json

class BNPLApiTests(TestCase):
    def setUp(self):
        # Create test data that runs before every test
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.customer = Customer.objects.create(user=self.user, credit_limit=500.00)

    def test_create_transaction(self):
        payload = {"customer_id": str(self.customer.id), "amount": 100.0}
        response = self.client.post(
            '/api/transactions',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())

    def test_activate_plan(self):
        # Create a transaction first
        tx = Transaction.objects.create(customer=self.customer, amount=100.0, status='PENDING')
        
        # Activate it
        response = self.client.post(f'/api/transactions/{tx.id}/activate')
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(BNPLPlan.objects.filter(transaction=tx).exists())

    def test_repayment_validation(self):
        # Setup: Create a plan
        tx = Transaction.objects.create(customer=self.customer, amount=100.0)
        plan = BNPLPlan.objects.create(transaction=tx, remaining_amount=100.0)
        
        # Try to pay more than owed
        payload = {"amount": 500.0}
        response = self.client.post(
            f'/api/plans/{plan.id}/repay',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        # Should return an error (or 200 depending on your error handling, 
        # but here we verify the logic)
        self.assertEqual(response.json().get('error'), "Payment exceeds remaining balance of 100.00")