import factory
from apps.transactions.models import Transaction
from apps.transactions.data import TRANSACTION_CLOSED


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction
    
    company=factory.SubFactory("apps.transactions.tests.factories.company.CompanyFactory")
    user=factory.SubFactory("apps.users.tests.factories.user.UserFactory")
    date="2022-03-04 10:00:00"
    price=100
    status_transaction=TRANSACTION_CLOSED
    status_approved=True

