from functools import wraps
from django.db import models
from .choices import CONTENT_LOCALE


class LocalizedModel(models.Model):
    """This is the abstract ancestor for all models, that contains multi
    language data, that doesn't make sense to put into i18n functional"""

    locale = models.CharField('Locale', max_length=2, default='ru',
                              choices=CONTENT_LOCALE)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Data and parameters of the {0} for {1} language'.format(type(self).__name__, self.locale)


def localised_classmethod(method):
    """The decorator that implements verification of locale
    before calling the serializer"""

    @wraps(method)
    def wrapper(cls, required_locale):

        validator = set()

        for item in CONTENT_LOCALE:
            validator.add(item[0])

        if not required_locale in validator:
            raise ValueError('The required locale didnt implemented!')

        return method(cls, required_locale)

    return wrapper
