from django.db import models
import uuid
from django.urls import reverse

class Student(models.Model):
    """
    Model representing a student
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Student Unique ID")
    first_name = models.CharField(max_length=200, help_text="Enter your first name.")
    last_name = models.CharField(max_length=200, help_text="Enter your last name.")
    progress = models.IntegerField()


    def __str__(self):
        """
        Returns full name
        """
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])


class Teacher(models.Model):
    """
    Model representing a teacher
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Teacher Unique ID")
    first_name = models.CharField(max_length=200, help_text="Enter your first name.")
    last_name = models.CharField(max_length=200, help_text="Enter your last name.")
    progress = models.IntegerField()
    student = models.ManyToManyField(Student, help_text="Select student name.")

    def __str__(self):
        """
        Returns full name
        """
        return '{0} {1}'.format(self.first_name, self.last_name)