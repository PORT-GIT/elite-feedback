from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from .models import Survey, SurveyResponse, Question, Choice
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin

#from .forms import SurveyForm, QuestionForm, SurveyResponseForm


# Create your views here.

def index(request):
    
    return render(request, 'feedbackapp/index.html')



# Create your views here.

def index(request):
    return render(request, 'feedbackapp/index.html')

def dashboard(request):
    return render(request, 'feedbackapp/dashboard.html')


#handles creating new survey then redirect QuestionCreateView
class SurveyCreateView(CreateView):
    model = Survey
    fields = '__all__'
    template_name = 'feedbackapp/survey_form.html'
    success_url = reverse_lazy('survey_list')

    def form_valid(self, form):
        messages.success(self.request, 'Survey created successfully!')
        return super().form_valid(form)

class SurveyListView(ListView):
    model = Survey
    template_name = 'feedbackapp/survey_list.html'

class SurveyDetailView(DetailView):
    model = Survey
    template_name = 'feedbackapp/survey_detail.html'

class SurveyDeleteView(DeleteView):
    model = Survey
    template_name = 'feedbackapp/survey_confirm_delete.html'
    success_url = reverse_lazy('survey_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Survey deleted successfully!')
        return super().delete(request, *args, **kwargs)

class SurveyUpdateView(UpdateView):
    model = Survey
    fields = '__all__'
    template_name = 'feedbackapp/survey_form.html'
    success_url = reverse_lazy('survey_list')

    def form_valid(self, form):
        messages.success(self.request, 'Survey updated successfully!')
        return super().form_valid(form)

#this will handle the creation of new questions
class QuestionCreateView(CreateView):
    model = Question
    fields = '__all__'
    template_name = 'feedbackapp/question_form.html'
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        messages.success(self.request, 'Question created successfully!')
        return super().form_valid(form)

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'feedbackapp/question_confirm_delete.html'
    success_url = reverse_lazy('question_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Question deleted successfully!')
        return super().delete(request, *args, **kwargs)

class QuestionListView(ListView):
    model = Question
    template_name = 'feedbackapp/question_list.html'

class QuestionUpdateView(UpdateView):
    model = Question
    fields = '__all__'
    template_name = 'feedbackapp/question_form.html'
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        messages.success(self.request, 'Question updated successfully!')
        return super().form_valid(form)

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'feedbackapp/question_detail.html'

#these are views for the feedback
class AnswerListView(ListView):
    model = SurveyResponse
    template_name = 'feedbackapp/answer_list.html'

class AnswerDetailView(DetailView):
    model = SurveyResponse
    template_name = 'feedbackapp/answer_detail.html'

class AnswerCreateView(CreateView):
    model = SurveyResponse
    fields = '__all__'
    template_name = 'feedbackapp/answer_form.html'
    success_url = reverse_lazy('answer_list')

    def form_valid(self, form):
        messages.success(self.request, 'Answer created successfully!')
        return super().form_valid(form)
    pass

class AnswerDeleteView(DeleteView):
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