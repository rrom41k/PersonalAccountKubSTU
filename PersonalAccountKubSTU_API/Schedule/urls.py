from django.urls import path, include
from .views import (
    InstituteListApiView,
    InstituteDetailApiView,
    DepartmentListApiView,
    DepartmentDetailApiView,
    SpecializationListApiView,
    SpecializationDetailApiView,
    GroupListApiView,
    GroupDetailApiView,
    StudentListApiView,
    StudentDetailApiView,
    SubjectListApiView,
    SubjectDetailApiView,
    ExamListApiView,
    ExamDetailApiView,
    EmployeeListApiView,
    EmployeeDetailApiView,
    LessonListApiView,
    LessonDetailApiView,
    Classes_SheldueListApiView,
    Classes_SheldueDetailApiView,
)

urlpatterns = [
    path('api/institute/', InstituteListApiView.as_view()),
    path('api/institute/<int:group_id>/', InstituteDetailApiView.as_view()),

    path('api/department/', DepartmentListApiView.as_view()),
    path('api/department/<int:group_id>/', DepartmentDetailApiView.as_view()),

    path('api/specialization/', SpecializationListApiView.as_view()),
    path('api/specialization/<int:specialization_id>/', SpecializationDetailApiView.as_view()),

    path('api/group/', GroupListApiView.as_view()),
    path('api/group/<int:group_id>/', GroupDetailApiView.as_view()),

    path('api/student/', StudentListApiView.as_view()),
    path('api/student/<int:student_id>/', StudentDetailApiView.as_view()),

    path('api/subject/', SubjectListApiView.as_view()),
    path('api/subject/<int:subject_id>/', SubjectDetailApiView.as_view()),

    path('api/exam/', ExamListApiView.as_view()),
    path('api/exam/<int:exam_id>/', ExamDetailApiView.as_view()),

    path('api/employee/', EmployeeListApiView.as_view()),
    path('api/employee/<int:employee_id>/', EmployeeDetailApiView.as_view()),

    path('api/lesson/', LessonListApiView.as_view()),
    path('api/lesson/<int:lesson_id>/', LessonDetailApiView.as_view()),

    path('api/classes_sheldue/', Classes_SheldueListApiView.as_view()),
    path('api/classes_sheldue/<int:classes_sheldue_id>/', Classes_SheldueDetailApiView.as_view()),
]
