from django.test import TestCase
from apps.transactions.models import Company, Transaction
from apps.users.models import User
from .factories.transaction import TransactionFactory
from .factories.company import CompanyFactory

class CompanyModelTest(TestCase):

    def setUp(self):
        self.company = CompanyFactory()

    def test_name(self):
        field_label = self.company._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        self.assertEquals(self.company.name, 'Plerk')

    def test_str(self):
        assert str(self.company) == "Plerk"


class TransactionModelTest(TestCase):

    def setUp(self):
        self.transaction = TransactionFactory()

    def test_price(self):
        field_label = self.transaction._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')
        self.assertEquals(self.transaction.price, 100)

    def test_status_transaction(self):
        field_label = self.transaction._meta.get_field('status_transaction').verbose_name
        self.assertEquals(field_label, 'status transaction')
        self.assertEquals(self.transaction.status_transaction, 'closed')

    def test_str(self):
        assert str(self.transaction) == f"{self.transaction.company} - {self.transaction.price}"
