from django.core.exceptions import ValidationError
from django.utils.translation import ugettext 
import re 

class CustomPasswortValidator(object):
    """ Валидатор паролей """
    def __init__(self, min_length=1, max_length=16):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, password, user=None):  
        if not any(char.isdigit() for char in password):
            raise ValidationError(('Password must contain at least %(min_length)d digit.') % {'min_length': self.min_length}) # Проверяет наличие цифр в пароле
        if len(password) > (int(self.max_length) - 1):
            raise ValidationError(('password must be up to %(max_length)d characters.') % {'max_length': self.max_length}) # Проверяет длину пароля
        if not any(char.isalpha() for char in password):
            raise ValidationError(('Password must contain at least %(min_length)d letter.') % {'min_length': self.min_length}) # Проверяет наличие букв в пароле
        if not '_' in password:
            raise ValidationError(('Password must contain at least %(min_length)d underscore.') % {'min_length': self.min_length}) # Проверяет наличие нижнего подчеркивания в пароле
        if not password[0].isupper():
            raise ValidationError('Password must start with uppercase letter.') # Проверяет, что пароль начинается с большой буквы



def validate_first_name(value):
    """ Валидация first_name"""
    if not re.match("^[A-Za-z-]*$", value):
        raise ValidationError("First Name can only contain letters and dashes.")



def validate_last_name(value):
    """ Валидация last_name"""
    if not re.match('^[A-Za-z- ]*$', value):
        raise ValidationError("Last Name name can only contain letters, dashes and whitespaces ") 


def validate_email_domain(value):
    """ Проверка email на наличие запрещенных доменов """
    if value.endswith('gmail.com') or value.endswith('icloud.com'):
        raise ValidationError("gmail.com and icloud.com does not support") #