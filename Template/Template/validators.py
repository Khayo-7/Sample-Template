from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_percentage(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not avalid. Percentile cannot be negative'),
            params={'value': value},
        )
    elif value > 100:
        raise ValidationError(
            _('%(value)s is not avalid. Percentile cannot be greater than 100.00 %'),
            params={'value': value},
        )

# def ip_validator(ip):

#     if     
# class PercentageField(fields.FloatField):
#     widget = fields.TextInput(attrs={"class": "percentInput"})

#     def to_python(self, value):
#         val = super(PercentageField, self).to_python(value)
#         if is_number(val):
#             return val/100
#         return val

#     def prepare_value(self, value):
#         val = super(PercentageField, self).prepare_value(value)
#         if is_number(val) and not isinstance(val, str):
#             return str((float(val)*100))
#         return val