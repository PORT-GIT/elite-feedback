from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Survey, SurveyResponse, Question, Choice
#from .forms import SurveyForm, QuestionForm, SurveyResponseForm


# Create your views here.

def index(request):
    
    return render(request, 'feedbackapp/index.html')

def dashboard(request):

    return render( request, 'feedbackapp/dashboard.html')

def employee_profile(request):

    return render (request, 'feedbackapp/employee-profile.html')

#handles creating new survey then redirect QuestionCreateView
#CHECK THE FOURTH CHAT FOR MORE EXPLANATION INTO VIEWS AND URLS
class SurveyCreateView(CreateView):
    pass

class SurveyListView(ListView):
    pass

class SurveyDetailView(DetailView):
    pass

class SurveyDeleteview(DeleteView):
    pass

class SurveyUpdateView(UpdateView):
    pass

#this will handle the creation of new questions
class QuestionCreateView(CreateView):
    pass

class QuestionDeleteView(DeleteView):
    pass

class QuestionListView(ListView):
    pass

class QuestionUpdateView(UpdateView):
    pass

class QuestionDetailView(DetailView):
    pass

#these are views for the feedback
class AnswerListView(ListView):
    pass

class AnswerDetailView(DetailView):
    pass

class AnswerCreateView(CreateView):
    pass