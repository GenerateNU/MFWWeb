from django.urls import path

from . import forms, views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('student_signup/', views.student_signup, name='student_signup'),
    path('frontpage/', views.frontpage, name='frontpage'),
    path('modules/', views.modules, name='modules'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('students/<int:id >', views.StudentDetailView.as_view(),
         name='student-detail'),
    path('students/', views.StudentDetailView.as_view(), name='student-detail'),
    path('prequiz/', views.prequiz, name='prequiz'),
    path('q1/', views.q1, name='q1'),
    path('q2/', views.q2, name='q2'),
    path('q3/', views.q3, name='q3'),
    path('q4/', views.q4, name='q4'),
    path('q5/', views.q5, name='q5'),
    path('q6/', views.q6, name='q6'),
    path('q7/', views.q7, name='q7'),
    path('q8/', views.q8, name='q8'),
    path('q9/', views.q9, name='q9'),
    path('q10/', views.q10, name='q10'),
    path('feedback/', views.feedback, name='feedback'),
    path('create_class/', views.create_class, name='create_class'),
    path('classes/', views.ClassListView.as_view(), name='classes'),
    path('class/<int:pk>', views.ClassDetailView.as_view(), name='class-detail'),
]
