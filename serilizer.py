from rest_framework import serializers
from backend.models import Person, Student, Faculty, ReadingMaterial, Face, Department, Course, Section, File

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('user', 'PID')

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('person', 'sectionList', 'faceList')

class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = ('person', 'sectionList')

class ReadingMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReadingMaterial
        fields = ('time', 'url', 'faculty', 'section')

class FaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Face
        fields = ('time', 'url')

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name', 'description')

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'dept', 'description')

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('no', 'course')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'type')
