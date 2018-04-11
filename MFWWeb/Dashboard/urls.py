from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('',views.index,name='index'),
    path('frontpage/',views.frontpage,name='frontpage'),
    path('modules/',views.modules,name='modules'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('students/<int:id >', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/', views.StudentDetailView.as_view(), name='student-detail'),
    path('simulation/', views.simulation, name='simulation'),
    path('q1/', views.ques, name='q1'),
    path('q2/', views.res, name='q2'),
    path('q3/', views.hyp, name='q3'),
    path('q4/', views.test, name='q4'),
    path('q5/', views.work, name='q5'),
    path('q6/', views.data, name='q6'),
    path('q7/', views.align, name='q7'),
    path('q9/', views.comm, name='q9'),
    path('done/', views.done, name='done'),
    path('feedback/', views.feedback, name='feedback'),
]
