from django.contrib import admin

from backend.models import Department, Course, Section, Face, Person, Student, Faculty, ReadingMaterial

# Register your models here.
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Face)
admin.site.register(ReadingMaterial)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Section)
