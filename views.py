from .serializer import PersonSerializer, StudentSerializer, FacultySerializer, ReadingMaterialSerializer, FaceSerializer, DepartmentSerializer, CourseSerializer, SectionSerializer, FileSerializer
from rest_framework import viewsets

from backend.models import Person, Student, Faculty, ReadingMaterial, Face, Department, Course, Section, File

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_fields = ('user', 'PID')

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_fields = ('person', 'sectionList', 'faceList')

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filter_fields = ('person', 'sectionList')

class ReadingMaterialViewSet(viewsets.ModelViewSet):
    queryset = ReadingMaterial.objects.all()
    serializer_class = ReadingMaterialSerializer
    filter_fields = ('time', 'url', 'faculty', 'section')

class FaceViewSet(viewsets.ModelViewSet):
    queryset = Face.objects.all()
    serializer_class = FaceSerializer
    filter_fields = ('time', 'url')

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_fields = ('id', 'name', 'description')

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_fields = ('id', 'dept', 'description')

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_fields = ('no', 'course')
