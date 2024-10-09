from django.db import models

#creating models
class Survey(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Question(models.Model):
    survey = models.ForeignKey(Survey)
    text = models.CharField(max_length=200, blank=False)
    question_type = models.CharField (max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Surveyresponse(models.Model):
    survey = models.ForeignKey(Survey)
    question = models.ForeignKey(Question)
    response = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

