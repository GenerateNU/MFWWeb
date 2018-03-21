from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('frontpage/',views.frontpage,name='frontpage'),
    path('modules/',views.modules,name='modules'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('students/<int:id >', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/', views.StudentDetailView.as_view(), name='student-detail'),
    path('quiz/',views.quiz,name='quiz'),
    path('quiz2a/',views.quiz2a,name='quiz2a'),
    path('quiz2b/',views.quiz2b,name='quiz2b'),
    path('quiz3a/',views.quiz3a,name='quiz3a'),
    path('quiz3b/',views.quiz3b,name='quiz3b'),
    path('quiz3c/',views.quiz3c,name='quiz3c'),
    path('quiz3d/',views.quiz3d,name='quiz3d'),
    path('feedback/', views.feedback, name='feedback'),
]
