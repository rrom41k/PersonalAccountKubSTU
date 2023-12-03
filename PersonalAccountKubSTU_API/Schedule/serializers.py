from rest_framework import serializers
from .models import Institute, Department, Specialization, Group, Student, Subject, Exam, Employee, Lesson, \
    Classes_Sheldue


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ["name", "content", "time_create", "time_update"]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["name", "content", "institute", "time_create", "time_update"]


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ["name", "number_specialization", "content", "department", "time_create", "time_update"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name", "specialization", "time_create", "time_update"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["login", "password", "name", "surname", "patronymic", "pas_data", "telephone", "email", "group",
                  "time_create", "time_update"]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["name", "specialization", "time_create", "time_update"]


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ["date_time_of_exam", "grading", "student", "subject", "time_create", "time_update"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["login", "password", "name", "surname", "patronymic", "pas_data", "telephone", "email", "department",
                  "time_create", "time_update"]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["number", "time_start", "time_end", "time_create", "time_update"]


class Classes_SheldueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes_Sheldue
        fields = ["classroom", "day_of_the_week", "group", "subject", "employee", "lesson", "time_create",
                  "time_update"]
