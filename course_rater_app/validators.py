from django.core.exceptions import ValidationError


def validate_session(array):
    """Assert that a session array formatted [date, period] is valid."""
    if len(array) != 2:
        raise ValidationError('A session must be length 2 (Format: [date, period])')

