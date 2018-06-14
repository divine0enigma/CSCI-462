from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Survey, Question, Response, Answer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse
from .forms import UserForm


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "CreateSurvey/index.html"
    context_object_name = 'all_surveys'

    def get_queryset(self):
        return Survey.objects.all()


class DetailsView(LoginRequiredMixin, generic.DetailView):
    model = Survey
    template_name = 'CreateSurvey/details.html'


class TakeSurvey(generic.DetailView):
    model = Response
    template_name = 'CreateSurvey/take-survey.html'


class ResponseCreate(CreateView):
    model = Response
    fields = []

    def form_valid(self, form):
        form.instance.survey_id = self.kwargs.get('pk')
        return super(ResponseCreate, self).form_valid(form)


def submit(request, pk):
    response = Response.objects.get(pk=pk)
    response.submitted = True
    response.save()
    return redirect(response)


class ResponseDelete(LoginRequiredMixin, DeleteView):
    model = Response

    def get_success_url(self, **kwargs):
        survey = self.object.survey
        return reverse_lazy("CreateSurvey:view-results", kwargs={'pk': survey.id})


class SurveyCreate(LoginRequiredMixin, CreateView):
    model = Survey
    fields = ['survey_title']


class SurveyUpdate(LoginRequiredMixin, UpdateView):
    model = Survey
    fields = ['survey_title']


class SurveyDelete(LoginRequiredMixin, DeleteView):
    model = Survey
    success_url = reverse_lazy('CreateSurvey:index')


class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question_field']

    def form_valid(self, form):
        form.instance.survey_id = self.kwargs.get('pk')
        return super(QuestionCreate, self).form_valid(form)


class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['question_field']


class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question

    def get_success_url(self, **kwargs):
        survey = self.object.survey
        return reverse_lazy("CreateSurvey:details", kwargs={'pk': survey.id})


class AnswerCreate(CreateView):
    model = Answer
    fields = ['answer_field']

    def form_valid(self, form):
        form.instance.response_id = self.kwargs.get('pk')
        form.instance.question_id = self.kwargs.get('question')
        return super(AnswerCreate, self).form_valid(form)


class AnswerUpdate(UpdateView):
    model = Answer
    fields = ['answer_field']


class AnswerDelete(DeleteView):
    model = Answer

    def get_success_url(self, **kwargs):
        response = self.object.response
        return reverse_lazy("CreateSurvey:take-survey", kwargs={'pk': response.id})


class ResultsView(generic.DetailView):
    model = Survey
    template_name = 'CreateSurvey/view-results.html'


class SurveyResults(generic.DetailView):
    model = Response
    template_name = 'CreateSurvey/survey-results.html'


def logout_view(request):
    logout(request)
    return redirect('CreateSurvey:index')


def login_view(request):
    logout(request)
    return redirect('CreateSurvey:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'CreateSurvey/registration.html'

    # blank form display
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('CreateSurvey:index')

        return render(request, self.template_name, {'form': form})