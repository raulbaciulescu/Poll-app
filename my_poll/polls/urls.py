from django.urls import path, include

from polls.views import indexx, QuestionsView, ChoicesView, ResultsView, CreateQuestion

app_name = 'polls'
urlpatterns = [
    path('', QuestionsView.as_view(), name='index'),
    path('questions/', QuestionsView.as_view(), name='question_list'),
    path('choice_list/<int:my_id>/', ChoicesView.as_view(), name='choice_list'),
    path('results/<int:my_id>/', ResultsView.as_view(), name='results'),
    path('create/', CreateQuestion.as_view(), name='create_question'),
]