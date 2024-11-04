from django.urls import path
from feedbackapp import views
from .views import SurveyCreateView, SurveyDeleteView, SurveyDetailView, SurveyListView, SurveyUpdateView, QuestionCreateView, QuestionDeleteView, QuestionListView, QuestionUpdateView, QuestionListView, QuestionDetailView, AnswerDetailView, AnswerListView, AnswerDeleteView


urlpatterns = [
    path('', views.index, name="index"),

    path('dashboard', views.dashboard, name="dashboard"),

    #path('employee-profile', views.employee_profile, name="employee-profile"),
    

    #these are urls for the surveys
    path('survey/', SurveyListView.as_view(), name='survey-list'),

    path('survey/create/', SurveyCreateView.as_view(), name='survey-create'),

    path('survey/edit/<int:pk>/', SurveyUpdateView.as_view(), name='survey-edit'),

    path('survey/delete/<int:pk>/', SurveyDeleteView.as_view(), name='survey-delete'),

    path('survey/details/<int:pk>/', SurveyDetailView.as_view(), name='survey-details'),


    #these are urls for the questions
    path('questions/', QuestionListView.as_view(), name='question-list'),

    path('questions/create/', QuestionCreateView.as_view(), name='questions-create'),

    path('questions/edit/<int:pk>/', QuestionUpdateView.as_view(), name='questions-edit'),

    path('questions/delete/<int:pk>/', QuestionDeleteView.as_view(), name='questions-delete'),

    path('questions/details/<int:pk>/', QuestionDetailView.as_view(), name='questions-details'),


    #these are the urls for the answers and feedback
    path('feedback/', AnswerListView.as_view(), name='feedback-list'),

    #path('feedback/create/', AnswerCreateView.as_view(), name='feedback-list'),

    path('feedback/details/<int:pk>/', AnswerDetailView.as_view(), name='feedback-details'),

    path('feedback/details/<int:pk>/', AnswerDeleteView.as_view(), name='feedback-delete'),
]