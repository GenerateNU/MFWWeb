from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Teacher
from django.shortcuts import render

ANSWER_1 = [
    ('correct', 'True'),
    ('incorrect', 'False'),
]


class Quiz(forms.Form):
    answer = forms.CharField(label='', widget=forms.RadioSelect(
        choices=ANSWER_1), required=False,)


class ClassForm(forms.Form):
    class_name = forms.CharField(label="Class name")


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = Teacher
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    class_code = forms.CharField(max_length=6, required=True)
