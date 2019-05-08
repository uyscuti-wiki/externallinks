from datetime import datetime
import factory
import random

from .models import LinkEvent, LinkSearchTotal, URLPattern


class URLPatternFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = URLPattern
        strategy = factory.CREATE_STRATEGY

    # factory.Faker returns a Faker object by default, rather than str
    url = str(factory.Faker('url', schemes=['https']))[8:-1]


class LinkEventFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LinkEvent
        strategy = factory.CREATE_STRATEGY

    timestamp = datetime.now()
    domain = "en.wikipedia.org"
    username = factory.Faker('user_name')
    rev_id = random.randint(10000000, 100000000)
    user_id = random.randint(10000000, 100000000)
    page_title = factory.Faker('word')
    page_namespace = 0
    event_id = factory.Faker('uuid4')
    change = random.choice([LinkEvent.ADDED, LinkEvent.REMOVED])
    on_user_list = False


class LinkSearchTotalFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LinkSearchTotal
        strategy = factory.CREATE_STRATEGY

    date = datetime.today()
    total = random.randint(1,1000)