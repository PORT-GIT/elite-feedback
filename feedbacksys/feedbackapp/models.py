from django.db import models
from customerapp.models import Customer
from employeeapp.models import SystemUsers
from django.core.exceptions import ValidationError
#raises errors when thenvalidation checks fail
from .validators import is_english, is_properly_capitalized

#creating models
class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    text = models.CharField(max_length=200, blank=False)
    question_type = models.CharField (max_length=200)
    created_at = models.DateField(auto_now_add=True)

    #this specifies the permissions that can be performed
    class Meta:
        permissions = [
            ("can_view_survey", "Can view survey"),
            ("can_edit_survey", "Can edit survey"),
            ("can_delete_survey", "Can delete survey"),
            ("can_send_survey","Can send survey"),
            ("can_respond_to_survey", "Can respond to survey"),
            ("can_create_survey", "Can create survey"),
        ]

        def __str__(self):
            return self.title
        
        
class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    #stores the actual question text
    question_type = models.CharField(max_length=200, choices=[('CHOICE', 'Multiple Choice'), ('OPEN-ENDED', 'Open-Ended')])
    #in the template is where i will give the conditional to create the choices or open-ended appear

    #specifies the actions that can be performed on the question or when creating the question
    class Meta:
        permissions = [
            ("can_view_question", "Can view question"),
            ("can_update_question", "Can update question"),
            ("can_delete_question", "Can delete question"),
            ("can_create_question", "Can create question"),
        ]

    def clean(self):
        #this is a method that performs validation check before saving to the database
        if not self.text:
            #checks if the rext field is empty
            raise ValidationError('Question text fields cannot be empty')
        
        if self.question_type not in dict(self._meta.get_field('question_type').choices):
            #checks if the question type is one of the defined choices
            raise ValidationError('Invalid question type')
        
        #these are in the validators file 
        is_english(self.text)
        is_properly_capitalized(self.text)
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    respondent = models.ForeignKey(Customer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    received_at = models.DateField(auto_now_add=True)

    #specifies the actions that can be performed on the feedback/response of the survey
    #or the model above
    class Meta:
        permissions = [
            
            ("can_view_feedback", "Can view feedback")
            ("can_submit_feedback_to_salon", "Can submit feedback to salon"),
            ("can_respond_to_feedback", "Can respond to feedback"),
            ("can_delete_feedback", "Can delete feedback"),
        ]

    
    


