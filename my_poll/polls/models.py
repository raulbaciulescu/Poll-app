from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=120)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.id} - {self.question_text}'

    def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return (self.pub_date <= timezone.now()) and (self.pub_date >= timezone.now() - datetime.timedelta(days=1))

    def get_absolute_url(self):
        return reverse('polls:choice_list', kwargs={'my_id': self.id})

    def get_absolute_url_results(self):
        return reverse('polls:results', kwargs={'my_id': self.id})

    def sum_of_votes(self):
        choices = Choice.objects.all()
        sum = 0
        for choice in choices:
            if choice.question == self:
                sum += choice.votes
        return sum


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

