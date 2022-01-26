from django.core.exceptions import ValidationError

class FirstDigitNotNumberValidator():
    
    def validate(self,password,user=None):
        if password[0].isdigit():
            raise ValidationError('First value must be a letter')
      
    def get_help_text(self):
        return "First value can't be a number"

class AtLeastOneUpperValidator():
    def validate(self,password,user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError('Password must contain at least one uppercase letter')
    def get_help_text(self):
        return "Must Contain One Uppercase Letter"
        
class AtLeastOneLowerValidator():
    def validate(self,password,user=None):
        if not any(char.islower() for char in password):
            raise ValidationError('Password must contain at least one lowercase letter')
        
    def get_help_text(self):
        return "Must Contain One Lowercase Letter"

class AtLeastOneSpecialValidator():
    special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
    def validate(self,password,user=None):
        if not any(char in self.special_characters for char in password):
            raise ValidationError(f"Password must contain at least one special {''.join(self.special_characters)} character.")
    def get_help_text(self):
        return "Must Contain One Special Character"