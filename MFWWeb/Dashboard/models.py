from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Student(User):
    """
    Model representing a student
    """
    progress = models.IntegerField()
    target_class = models.ForeignKey('Class', on_delete=models.CASCADE, null=True)

    def __str__(self):
        """
        Returns full name
        """
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])


class Teacher(User):
    """
    Model representing a teacher
    """

    def __str__(self):
        """
        Returns full name
        """
        return '{0} {1}'.format(self.first_name, self.last_name)


class Class(models.Model):
    """
    Model representing a class
    """
    name = models.CharField(max_length=200, help_text="Enter a classroom name.")
    students = models.ManyToManyField(Student, help_text="Select student name.")
    teacher = models.ForeignKey(Teacher, default=1, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default=get_random_string(length=6))

    def __str__(self):
        """
        Returns class name
        """
        return '{0}'.format(self.name)

    def get_absolute_url(self):
        return reverse('class-detail', args=[str(self.id)])


class Quiz(models.Model):
    question1_answers = (
        ('T', 'True'),
        ('F', 'False'),
    )

    question2_answers = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    question1 = models.CharField(max_length=200, help_text="True or False: Malaria is bad")
    question2 = models.CharField(max_length=200, help_text="Enter your last name.")
