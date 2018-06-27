from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager


class Question(models.Model):
    # The user asking the question. Only the user or an Admin can select
    # select an answer
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # A short description of the question
    title = models.CharField(max_length=255)
    # Details of a question to provide context and share what attempts
    # of a solution have been made.
    body = models.TextField()
    # A score that rates the usefulness of a question
    score = models.IntegerField(blank=True, default=0)

    # Labels and keywords that the user can provide to categorize a question
    # and support easier searching of questions
    tags = TaggableManager()


class Answer(models.Model):
    # The user answering the question
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # The question to which the answer was provided
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # The answer
    body = models.TextField()
    # Answers are ranked and sorted on the page in order of rink. This allows
    # for the best answers to be shown first.
    score = models.IntegerField(blank=True, default=0)