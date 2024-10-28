#THIS IS A VALIDATORE FOR THE PHONE NUMBER MODEL FIELD IN THE APP'S MODELS.PY FILE
from django.core.exceptions import ValidationError
from phonenumbers import parse, is_valid_number

def phonenumber_validation(value):
    #this is a function
    try:
        #checks the region of the phonenumber is accurate
        phone_number = parse(value, "KE")
        #specifies that the number should be treated like a Kenyan number
        if not is_valid_number(phone_number):
            #if not the error below is raised
            raise ValidationError("Invalid phone number")
        national_number=str(phone_number.national_number)
        #this line means that part of the phone number is extracted which is used locally
        #separate from the country code
        
        if len(national_number) < 9 or len(national_number) > 10:
            raise ValidationError("Invalid: Phone number must not be longer 10 digits only")
        
    except Exception as e:
        raise ValidationError("Invalid phone number format")
        
        
    
