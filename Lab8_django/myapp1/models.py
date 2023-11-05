from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Students(models.Model):
    Student_id = models.AutoField(primary_key=True)
    Student_surname = models.CharField(max_length=255)
    Student_name = models.CharField(max_length=255)
    Student_lastname = models.CharField(max_length=255)
    Student_address = models.CharField(max_length=255)
    Student_phone = models.CharField(max_length=15)
    Course = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    Faculty = models.CharField(max_length=50, choices=[('аграрного менеджменту', 'аграрного менеджменту'), ('економіки', 'економіки'), ('інформаційних технологій', 'інформаційних технологій')])
    Student_group = models.CharField(max_length=10)
    isHead = models.BooleanField()

    def get_full_name(self):
        return f"{self.Student_surname} {self.Student_name} {self.Student_lastname}"


class Subjects(models.Model):
    Subject_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Hours_per_semester = models.PositiveIntegerField()
    Number_of_semesters = models.PositiveIntegerField()

    def __str__(self):
        return self.Title

class Passing_exams(models.Model):
    Passing_id = models.AutoField(primary_key=True)
    Date_of_passing = models.DateField()
    Student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    Subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Score = models.PositiveIntegerField(validators=[MinValueValidator(2), MaxValueValidator(5)])
