from django.test import TestCase
import datetime

from django.urls import reverse
from django.utils import timezone


# Create your tests here.
from polls.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionIndexViewTests(TestCase):
    def create_question(self, question_text, days):
        time = timezone.now() + + datetime.timedelta(days=days)
        Question.objects.create(question_text=question_text, pub_date=time)

    def test_no_questions(self):
        response = self.client.get(reverse('polls:question_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['objects']), [])

    # def test_questions(self):
    #     response = self.client.get(reverse('polls:question_list'))
    #     question = self.create_question(question_text='text1', days=30)
    #
    #     self.assertEqual(response.status_code, 200)
    #     print('ccccccccccccc', list(response.context['objects']))
    #     #self.assertQuerysetEqual(list(response.context['objects']), [question])