from django.shortcuts import render
from myapp1.models import Students, Subjects, Passing_exams

def index_page(request):
    students = Students.objects.all()
    subjects = Subjects.objects.all()
    passing_exams = Passing_exams.objects.all()

    context = {
        'students': students,
        'subjects': subjects,
        'passing_exams': passing_exams,
        'project_name': 'Лаб 8',
        'student_info': 'Бабій Богдан Юрійович, КН-20002б',
    }

    return render(request, 'index.html', context)
