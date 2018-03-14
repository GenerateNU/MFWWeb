from django import forms

'''
FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class QuizForm(forms.Form):
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
'''

ANSWER_1= [
    ('a', 'true'),
    ('false', 'false'),
    ]

ANSWER_2a= [
    ('a', 'because I think so'),
    ('b', 'because malaria can kill people'),
    ]
ANSWER_2b= [
    ('a', 'i am sure'),
    ('b', 'i am not sure'),
    ]

ANSWER_3a= [
    ('a', 'i dont want to'),
    ('b', 'i did research'),
    ]

ANSWER_3b= [
    ('a', 'ok ill try'),
    ('b', 'i cannot'),
    ]

ANSWER_3c= [
    ('a', 'ya'),
    ('b', 'nah'),
    ]

ANSWER_3d= [
    ('a', 'i know'),
    ('b', 'oops'),
    ]




class Quiz(forms.Form):
    answer = forms.CharField(label='True or false, malaria is bad', widget=forms.RadioSelect(choices=ANSWER_1), required= False,)
    '''answer = forms.ChoiceField(widget = forms.Select(),
                     choices = ([('1','1'), ('2','2'),('3','3'), ]), initial='3', required = False,)'''

class Quiz2a(forms.Form):
    answer2a = forms.CharField(label='Why do you think malaria is bad?', widget=forms.RadioSelect(choices=ANSWER_2a), required= False,)

class Quiz2b(forms.Form):
    answer2b = forms.CharField(label='Are you sure you think that Malaria is not bad?', widget=forms.RadioSelect(choices=ANSWER_2b), required= False,)

class Quiz3a(forms.Form):
    answer3a = forms.CharField(label='you have to give me a reason', widget=forms.RadioSelect(choices=ANSWER_3a), required= False,)

class Quiz3b(forms.Form):
    answer3b = forms.CharField(label='yes that is bad. you should do something about that', widget=forms.RadioSelect(choices=ANSWER_3b), required= False,)

class Quiz3c(forms.Form):
    answer3c = forms.CharField(label='glad you are sure. is your friend sure?', widget=forms.RadioSelect(choices=ANSWER_3c), required= False,)

class Quiz3d(forms.Form):
    answer3d = forms.CharField(label='that is not good. you should be sure, bc malaria is actually bad', widget=forms.RadioSelect(choices=ANSWER_3d), required= False,)
