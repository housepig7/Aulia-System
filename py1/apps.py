from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class Py1Config(AppConfig):
    name = 'py1'


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'