from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
# Create your views here.
from polls.form import QuestionForm
from polls.models import Question, Choice
from django.http import Http404
from django.utils import timezone

class MakeContext:
    def make_context(self, my_id=None):
        choices = Choice.objects.all()
        context = {
            'question': Question.objects.get(id=my_id),
            'objects': []
        }
        for choice in choices:
            if choice.question == Question.objects.get(id=my_id):
                context['objects'].append(choice)

        if context['objects'] == []:
            context['objects'] = [True]

        return context

def indexx(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class QuestionsView(View):
    template_name = 'question_list.html'
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        context ={
            'objects': Question.objects.all()
        }
        return render(request, self.template_name, context)

class ChoicesView(MakeContext, View):
    template_name = 'choice_list.html'

    def get(self, request, my_id=None, *args, **kwargs):
        return render(request, self.template_name, self.make_context(my_id))


    def post(self, request, my_id=None, *args, **kwargs):
        #update votes
        try:
            choice = Choice.objects.get(pk=request.POST['choice'])
            choice.votes += 1
            choice.save()
        except:
            return render(request, self.template_name, self.make_context(my_id))

        return redirect(reverse('polls:results', kwargs={'my_id': my_id}))

class ResultsView(MakeContext, View):
    template_name = 'result.html'
    def get(self, request, my_id=None, *args, **kwargs):
        return render(request, self.template_name,  self.make_context(my_id))

class CreateQuestion(View):
    template_name = 'create_question.html'

    def get(self, request, *args, **kwargs):
        form = QuestionForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            q = Question(question_text=form.cleaned_data['question_text'], pub_date=timezone.now())
            q.save()
            Choice.objects.create(question=q, choice_text=form.cleaned_data['choice1'])
            Choice.objects.create(question=q, choice_text=form.cleaned_data['choice2'])
            Choice.objects.create(question=q, choice_text=form.cleaned_data['choice3'])
        #return redirect('polls:question_list')
        context = {
            'form': form
        }
        return redirect(reverse('polls:question_list'))






