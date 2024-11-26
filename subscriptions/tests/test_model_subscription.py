from django.test import TestCase
from datetime import datetime
from subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='JosÉ Filipe',
            cpf='12345678901',
            email='jfmarques0909.shadow@gmail.com',
            phone='53-12345-6789'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Eduardo', str(self.obj))
