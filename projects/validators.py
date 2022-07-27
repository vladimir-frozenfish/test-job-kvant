from django.core.exceptions import ValidationError


def priority(value):
    if value > 100:
        raise ValidationError('Приоритет должен быть от 0 до 100')