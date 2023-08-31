from django.core.exceptions import ValidationError


def validate_password(value):
    if not len(value)> 5:
        raise ValidationError("The password needs to be at least 8 characters long")