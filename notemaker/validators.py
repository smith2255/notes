from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def min_length_three(value):
    if len(value) < 3:
        raise ValidationError(
            _('%(value)s has less than three characters'),
            params={'value': value},
        )
