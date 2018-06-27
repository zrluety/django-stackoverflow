from django.urls import path

from question_answer import views

urlpatterns = [
    path('ask/', views.QuestionCreate.as_view(), name='question-create'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
]