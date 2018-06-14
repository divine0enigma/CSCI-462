from django.db import models
from django.urls import reverse
import uuid
from pgcrypto_expressions.fields import EncryptedTextField


class Survey(models.Model):
    survey_title = models.CharField(max_length=500)
    # anonymous = models.BooleanField(default=False)

    def __str__(self):
        return str(self.survey_title)

    def get_absolute_url(self):
        return reverse('CreateSurvey:details', kwargs={'pk': self.pk})


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_field = models.CharField(max_length=500)
    # encrypted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.question_field)

    def get_absolute_url(self):
        return reverse('CreateSurvey:details', kwargs={'pk': self.survey_id})


class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    interview_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    submitted = models.BooleanField(default=False)

    def __unicode__(self):
        return "response %s" % self.interview_uuid

    def get_absolute_url(self):
        return reverse('CreateSurvey:take-survey', kwargs={'pk': self.pk, 'survey': self.survey_id})


class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_field = EncryptedTextField(max_length=500)

    class Meta:
        unique_together = ('response', 'question')

    def __str__(self):
        return str(self.answer_field)

    def get_absolute_url(self):
        return reverse('CreateSurvey:take-survey', kwargs={'pk': self.response_id, 'survey': self.response.survey_id})
