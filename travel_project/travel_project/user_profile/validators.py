import re
from django.core.exceptions import ValidationError


def validate_profile_name(value):
    if not re.match(r'^[A-Za-z\s]+$', value):
        raise ValidationError("The name must contain letters only!")


def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError("The phone number must contain digit only!")