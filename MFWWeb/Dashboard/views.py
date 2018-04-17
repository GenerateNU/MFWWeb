import random

from django import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import FormView
from django.shortcuts import get_list_or_404, get_object_or_404
from .forms import ClassForm, Quiz, SignUpForm, StudentForm
from .models import Class, Student, Teacher

one = ['Ask a Question 1', 'Ask a Question 2',
       'Ask a Question 3', 'Ask a Question 4']
two = ["Research 1", "Research 2", "Research 3", "Research 4", "Research 5",
       "Research 6", "Research 7", "Research 8", "Research 9", "Research 10"]
three = ["Hypothesis 1", "Hypothesis 2", "Hypothesis 3", "Hypothesis 4"]
four = ["Experiment 1", "Experiment 2", "Experiment 3", "Experiment 4", "Experiment 5",
        "Experiment 6", "Experiment 7", "Experiment 8", "Experiment 9", "Experiment 10"]
five = ["Is the procedure working?"]
six = ["Analyze Data 1", "Analyze Data 2", "Analyze Data 3", "Analyze Data 4", "Analyze Data 5",
       "Analyze Data 6", "Analyze Data 7", "Analyze Data 8", "Analyze Data 9", "Analyze Data 10"]
seven = ["Results align 1", "Results align 2", "Results align 3", "Results align 4", "Results align 5",
         "Results align 6", "Results align 7", "Results align 8", "Results align 9", "Results align 10"]
eight = ["Results do not align 1", "Results do not align 2", "Results do not align 3", "Results do not align 4", "Results do not align 5",
         "Results do not align 6", "Results do not align 7", "Results do not align 8", "Results do not align 9", "Results do not align 10"]
nine = ["Communicate results 1", "Communicate results 2", "Communicate results 3", "Communicate results 4", "Communicate results 5",
        "Communicate results 6", "Communicate results 7", "Communicate results 8", "Communicate results 9", "Communicate results 10"]
responses = ['', '', '', '', '', '', '', '', '', '']
questions = ['', '', '', '', '', '', '', '', '', '']
# Create your views here.


def index(request):
    """
    View function for the index of the site.
    """
    num_students = Student.objects.all().count()
    num_teachers = Teacher.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_students': num_students,
                 'num_teachers': num_teachers}
    )


class StudentListView(generic.ListView):
    model = Student


class TeacherListView(generic.ListView):
    model = Teacher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            context['classes'] = Class.objects.filter(teacher=self.request.user)
        return context


class ClassListView(generic.ListView):
    model = Class


class ClassDetailView(generic.DetailView):
    model = Class


def class_detail_view(request,pk):
    class_id = get_object_or_404(Class, pk=pk)
    students = Student.objects.filter(target_class=class_id)
    print(students)

    return render(
        request,
        'class/class_detail.html',
        context={'class': class_id, 'students': students}
    )


class StudentDetailView(generic.DetailView):
    model = Student


def modules(request):
    """
    View function for the index of the site.
    """
    return render(
        request,
        'modules.html',
        context={}
    )


def homepage(request):
    """
    View function for the index of the site.
    """
    return render(
        request,
        'homepage.html',
        context={}
    )


def prequiz(request):
    answer = ''
    num = 0
    question = "Bednets (T) or Wells (F)"
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q1(request):
    answer = ''
    num = 1
    question = one[random.randint(0, len(one) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q2(request):
    answer = ''
    num = 2
    question = two[random.randint(0, len(two) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q3(request):
    answer = ''
    num = 3
    question = three[random.randint(0, len(three) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q4(request):
    answer = ''
    num = 4
    question = four[random.randint(0, len(four) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q5(request):
    answer = ''
    num = 5
    question = five[random.randint(0, len(five) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q6(request):
    answer = ''
    num = 6
    question = six[random.randint(0, len(six) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q7(request):
    answer = ''
    num = 7
    question = seven[random.randint(0, len(seven) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q8(request):
    answer = ''
    num = 8
    question = eight[random.randint(0, len(eight) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q9(request):
    answer = ''
    num = 9
    question = nine[random.randint(0, len(nine) - 1)]
    questions[num] = question
    submitbutton = request.POST.get("Submit")
    form = Quiz(request.POST)
    if form.is_valid():
        answer = form.cleaned_data.get("answer")
        responses[num] = answer
    return render(
        request,
        'quiz.html',
        {'form': form, 'answer': answer, 'submitbutton': submitbutton,
         'question': question, 'num': num}
    )


def q10(request):
    data = responses
    return render(
        request,
        'done.html',
        {'responses': responses, 'questions': questions}
    )


def frontpage(request):
    """
    View function for the index of the site.
    """
    return render(
        request,
        'frontpage.html',
        context={}
    )


def feedback(request):
    return render(
        request,
        'feedback.html',
        context={}
    )


def create_class(request):
    form = ClassForm(request.POST)
    if form.is_valid():
        class_name = form.cleaned_data.get("class_name")
        new_class = Class(name=class_name, teacher=request.user)
        new_class.save()
        return redirect('teachers')
    return render(
        request, 'Dashboard/create_class.html', {'form': form}
    )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('teachers')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def student_signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            class_code = form.cleaned_data.get('class_code')
            target_class = Class.objects.get(code=class_code)
            student = Student(first_name=first_name, last_name=last_name, target_class=target_class, progress=0)
            student.save()
            return redirect('homepage')
    else:
        form = StudentForm()
    return render(request, 'registration/student_signup.html', {'form': form})
