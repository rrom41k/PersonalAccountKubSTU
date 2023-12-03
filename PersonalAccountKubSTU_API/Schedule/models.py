from django.db import models


class Institute(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    institute = models.ForeignKey('Institute', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=255)
    number_specialization = models.CharField(max_length=255, null=False)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    department = models.ForeignKey('Department', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    specialization = models.ForeignKey('Specialization', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True)
    pas_data = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{str.upper(self.surname)} {str.upper(self.name)}.{str.upper(self.patronymic)}'


class Subject(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    specialization = models.ForeignKey('Specialization', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name


class Exam(models.Model):
    date_time_of_exam = models.DateTimeField()
    grading = models.CharField(max_length=1)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    student = models.ForeignKey('Student', on_delete=models.PROTECT, null=False)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, null=False)


class Employee(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True)
    pas_data = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    department = models.ForeignKey('Department', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f'{str.upper(self.surname)} {str.upper(self.name)}.{str.upper(self.patronymic)}'


class Lesson(models.Model):
    number = models.CharField(max_length=1)
    time_start = models.CharField(max_length=5)
    time_end = models.CharField(max_length=5)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{str(self.number)} {str(self.time_start)}.{str(self.time_end)}'


class Classes_Sheldue(models.Model):
    classroom = models.CharField(max_length=10)
    day_of_the_week = models.CharField(max_length=30)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=False)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, null=False)
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, null=False)
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT, null=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
