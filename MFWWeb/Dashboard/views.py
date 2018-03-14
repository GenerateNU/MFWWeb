from django.shortcuts import render
from .models import Student, Teacher
from django.views import generic


# Create your views here.
def index(request):
    """
    View function for the index of the site.
    """
    num_students=Student.objects.all().count()
    num_teachers=Teacher.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_students':num_students,
                 'num_teachers':num_teachers}
    )

class StudentListView(generic.ListView):
    model = Student

class TeacherListView(generic.ListView):
    model = Teacher


class StudentDetailView(generic.DetailView):
    model = Student

    def book_detail_view(request,pk):
        try:
            book_id=Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

            #book_id=get_object_or_404(Book, pk=pk)

        return render(
            request,
            'catalog/book_detail.html',
            context={'book':book_id,}
        )

def modules(request):
    """
    View function for the index of the site.
    """
    return render(
        request,
        'modules.html',
        context={}
    )
<<<<<<< HEAD
'''
def quiz(request):

    return render(
        request,
        'quiz.html',
        context={}
    )'''
"""
def quiz(request):
    firstname= request.POST.get('Firstname')

    lastname= request.POST.get('Lastname')

    answer= request.POST.get('true')

    answer1= request.POST.get('false')

    city= request.POST.get('City')

    state= request.POST.get('State')

    submitbutton= request.POST.get('Submit')
    form= QuizForm(request.POST)
    if form.is_valid():
        favoritefruit= form.cleaned_data.get("favorite_fruit")

    context= {'form': form, 'favoritefruit': favoritefruit, 'firstname': firstname, 'lastname': lastname, 'answer': answer, 'answer1': answer1,
              'city': city, 'state': state,
              'submitbutton': submitbutton}

    return render(request, 'quiz.html', context)
    """


from .forms import Quiz
from .forms import Quiz2a
from .forms import Quiz2b
from .forms import Quiz3a
from .forms import Quiz3b
from .forms import Quiz3c
from .forms import Quiz3d
def quiz(request):
    submitbutton= request.POST.get("submit")

    answer=''

    form= Quiz(request.POST)
    if form.is_valid():
        answer=form.cleaned_data.get("answer")


    context= {'form': form, 'submitbutton': submitbutton, 'answer': answer}

    return render(request, 'quiz.html', context)

def quiz2a(request):
    submitbutton= request.POST.get("submit")

    answer2a=''

    form= Quiz2a(request.POST)
    if form.is_valid():
        answer2a=form.cleaned_data.get("answer2a")


    context= {'form': form, 'submitbutton': submitbutton, 'answer2a': answer2a}

    return render(request, 'quiz2a.html', context)

def quiz2b(request):
    submitbutton= request.POST.get("submit")

    answer2b=''

    form= Quiz2b(request.POST)
    if form.is_valid():
        answer2b=form.cleaned_data.get("answer2b")


    context= {'form': form, 'submitbutton': submitbutton, 'answer2b': answer2b}

    return render(request, 'quiz2b.html', context)

def quiz3a(request):
    submitbutton= request.POST.get("submit")

    answer3a=''

    form= Quiz3a(request.POST)
    if form.is_valid():
        answer3a=form.cleaned_data.get("answer3a")


    context= {'form': form, 'submitbutton': submitbutton, 'answer3a': answer3a}

    return render(request, 'quiz3a.html', context)


def quiz3b(request):
    submitbutton= request.POST.get("submit")

    answer3b=''

    form= Quiz3b(request.POST)
    if form.is_valid():
        answer3b=form.cleaned_data.get("answer3b")


    context= {'form': form, 'submitbutton': submitbutton, 'answer3b': answer3b}

    return render(request, 'quiz3b.html', context)

def quiz3c(request):
    submitbutton= request.POST.get("submit")

    answer3c=''

    form= Quiz3c(request.POST)
    if form.is_valid():
        answer3c=form.cleaned_data.get("answer3c")


    context= {'form': form, 'submitbutton': submitbutton, 'answer3c': answer3c}

    return render(request, 'quiz3c.html', context)

def quiz3d(request):
    submitbutton= request.POST.get("submit")

    answer3d=''

    form= Quiz3d(request.POST)
    if form.is_valid():
        answer3d=form.cleaned_data.get("answer3d")


    context= {'form': form, 'submitbutton': submitbutton, 'answer3d': answer3d}

    return render(request, 'quiz3d.html', context)









def frontpage(request):
        """
        View function for the index of the site.
        """
        return render(
            request,
            'frontpage.html',
            context={}
        )
=======

def feedback(request):
    """
    View function for the index of the site.
    """
    return render(
        request,
        'feedback.html',
        context={}
    )
>>>>>>> 896509d72268644083480d61b6f9b4055ca60ea0
