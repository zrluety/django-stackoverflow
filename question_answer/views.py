from django.views.generic import CreateView
from django.views.generic.detail import DetailView

from question_answer.models import Question


class QuestionCreate(CreateView):
    model = Question
    fields = ['title', 'body', 'tags']


class QuestionDetailView(DetailView):
    model = Question
