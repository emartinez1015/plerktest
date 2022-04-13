import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = email = factory.Sequence(lambda n: "user_{}@plerk.io".format(n))
    username = factory.Sequence(lambda n: "user_{}".format(n))