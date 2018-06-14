from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import logout

app_name = 'CreateSurvey'

urlpatterns = [

    # creation homepage
    path('', views.IndexView.as_view(), name='index'),

    # registration
    path('registration/', views.UserFormView.as_view(), name='registration'),

    # login
    path('login/', views.login_view, name='login'),

    # logout
    path('logout/', views.logout_view, name='logout'),

    # specific survey
    path('survey/<pk>/', views.DetailsView.as_view(), name='details'),

    # create survey
    path('survey-add/', views.SurveyCreate.as_view(), name='survey-add'),

    # create question
    path('survey/<pk>/question-add/', views.QuestionCreate.as_view(), name='question-add'),

    # update survey
    path('survey/<pk>/update-survey/', views.SurveyUpdate.as_view(), name='survey-update'),

    # update question
    path('survey/<survey>/update-question/<pk>', views.QuestionUpdate.as_view(), name='question-update'),

    # delete survey
    path('survey/<pk>/delete-survey/', views.SurveyDelete.as_view(), name='survey-delete'),

    # delete question
    path('survey/<survey>/delete-question/<pk>', views.QuestionDelete.as_view(), name='question-delete'),

    # add response
    path('survey/<pk>/response-add/', views.ResponseCreate.as_view(), name='response-add'),

    # submit response
    path('survey/response-submit/<pk>', views.submit, name='response-submit'),

    # delete response
    path('survey/<survey>/survey-results/', views.SurveyResults.as_view(), name='survey-results'),
    path('survey/<survey>/response-delete/<pk>', views.ResponseDelete.as_view(), name='response-delete'),

    # specific take-survey
    path('survey/<survey>/take-survey/<pk>', views.TakeSurvey.as_view(), name='take-survey'),

    # add answer
    path('take-survey/<pk>/answer-add/', views.AnswerCreate.as_view(), name='answer-add'),
    path('take-survey/<pk>/answer-add/<question>', views.AnswerCreate.as_view(), name='answer-add'),

    # update answer
    path('take-survey/<response>/update-answer/<pk>', views.AnswerUpdate.as_view(), name='answer-update'),

    # delete answer
    path('take-survey/<response>/delete-answer/<pk>', views.AnswerDelete.as_view(), name='answer-delete'),

    # view results
    path('survey/<pk>/view-results', views.ResultsView.as_view(), name='view-results'),

    # survey result
    path('survey/<survey>/survey-results/', views.SurveyResults.as_view(), name='survey-results'),
    path('survey/<survey>/survey-results/<pk>', views.SurveyResults.as_view(), name='survey-results')

]

urlpatterns += staticfiles_urlpatterns()