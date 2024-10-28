#this file is being used to validation the models for the survey
#creation models and forms
#Validations put in place include:
#1. Ensure that the survey is not empty in the database
#2. ensure that the survey is created in english
#3. ensure that the question is not empty

import re
from django.core.exceptions import ValidationError


def is_english(self, text):
        #expression to check if text is english
        pattern = r'^[a-zA-Z\s\.,!?]+$'
        if not re.match(pattern, text):
              raise ValidationError('Please enter text in english')
        
       
def is_properly_capitalized(self, text):
    #expression to check if text is properly capitalized
    pattern = r'^[A-Z][a-z\s\.,!?]*$'
    if not re.match(pattern, text):
          raise ValidationError('Please capitalize first letter of text')
    
   