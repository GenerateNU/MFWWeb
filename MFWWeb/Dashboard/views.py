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
    def get_queryset(self):
        return Student.objects.all()

class StudentDetailView(generic.DetailView):
    model = Student
