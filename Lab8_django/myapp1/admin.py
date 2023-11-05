from django.contrib import admin
from .models import Students, Subjects, Passing_exams

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    pass

@admin.register(Passing_exams)
class PassingExamsAdmin(admin.ModelAdmin):
    pass
