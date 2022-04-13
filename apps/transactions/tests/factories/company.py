import factory
from apps.transactions.models import Company


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company
    
    name='Plerk'
    active_status=True