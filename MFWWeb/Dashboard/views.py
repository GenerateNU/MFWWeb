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
    """
    def get_queryset(self):
        Student.objects.all() """

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
