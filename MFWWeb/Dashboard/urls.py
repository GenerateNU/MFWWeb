from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('students/<int:id >', views.StudentDetailView.as_view(), name='student-detail'),
    path('students/', views.StudentDetailView.as_view(), name='student-detail'),

]
