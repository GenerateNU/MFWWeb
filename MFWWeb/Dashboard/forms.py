from django import forms
from django.shortcuts import render

ANSWER_1= [
    ('correct', 'True'),
    ('incorrect', 'False'),
    ]

class Quiz(forms.Form):
    answer= forms.CharField(label = '', widget=forms.RadioSelect(choices=ANSWER_1), required= False,)

class ClassForm(forms.Form):
    class_name = forms.CharField(label="Class name")
