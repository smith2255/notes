from .. import validators
from django.core.exceptions import ValidationError
from django.test import TestCase


class MinLengthOfThreeValidatorTest(TestCase):

    def test_under_three(self):
        string = "HI"
        with self.assertRaises(ValidationError):
            validators.min_length_three(string)

    def test_at_three(self):
        string = "TDO"
        validators.min_length_three(string)

    def test_over_three(self):
        string = "My Note!"
        validators.min_length_three(string)
