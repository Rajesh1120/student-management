from django.db import models

class Student(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
    ]
    GENDER_CHOICES=[
        ("Male", "Male"),
        ("Female","Female")
    ]
    id=models.AutoField(primary_key=True)
    student_roll_no = models.CharField(max_length=10, unique=True)
    student_name = models.CharField(max_length=100)
    student_branch = models.CharField(max_length=100,choices=BRANCH_CHOICES)
    student_gender = models.CharField(max_length=10,choices=GENDER_CHOICES)

    def __str__(self):
        return self.student_name
