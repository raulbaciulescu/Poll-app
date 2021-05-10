

from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(label='', max_length=120, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'rows': 10,
        'id': 'question',
    }))
    choice1 = forms.CharField(label='Choice 1', max_length=120, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'rows': 10,
        'id': 'question',
    }))
    choice2 = forms.CharField(label='Choice 2', max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'rows': 10,
        'id': 'question',
    }))
    choice3 = forms.CharField(label='Choice 3', max_length=120, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'rows': 10,
        'id': 'question',
    }))
