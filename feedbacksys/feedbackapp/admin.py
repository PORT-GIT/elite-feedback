from django.contrib import admin
from .models import Survey, Question, SurveyResponse, Choice

admin.site.register(Survey)
admin.site.register(SurveyResponse)
admin.site.register(Question)
admin.site.register(Choice)