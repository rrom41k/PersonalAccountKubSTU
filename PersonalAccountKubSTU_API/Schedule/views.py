from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import (Institute, Department, Specialization, Group, Student, Subject, Exam, Employee, Lesson,
                     Classes_Sheldue)
from .serializers import (InstituteSerializer, DepartmentSerializer, SpecializationSerializer, GroupSerializer,
                          StudentSerializer, SubjectSerializer, ExamSerializer, EmployeeSerializer, LessonSerializer,
                          Classes_SheldueSerializer)


class InstituteListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Institute items for given requested user
        '''
        institutes = Institute.objects
        serializer = InstituteSerializer(institutes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Institute with given institute data
        '''
        data = {
            'name': request.data.get('name'),
            'content': request.data.get('content')
        }
        serializer = InstituteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InstituteDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, institute_id):
        '''
        Helper method to get the object with given institute_id
        '''
        try:
            return Institute.objects.get(id=institute_id)
        except Institute.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, institute_id, *args, **kwargs):
        '''
        Retrieves the Institute with given institute_id
        '''
        institute_instance = self.get_object(institute_id)
        if not institute_instance:
            return Response(
                {"res": "Object with institute id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = InstituteSerializer(institute_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, institute_id, *args, **kwargs):
        '''
        Updates the institute item with given institute_id if exists
        '''
        institute_instance = self.get_object(institute_id)
        if not institute_instance:
            return Response(
                {"res": "Object with institute id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'content': request.data.get('specialization')
        }
        serializer = InstituteSerializer(instance=institute_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, institute_id, *args, **kwargs):
        '''
        Deletes the institute item with given institute_id if exists
        '''
        institute_instance = self.get_object(institute_id)
        if not institute_instance:
            return Response(
                {"res": "Object with institute id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        institute_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class DepartmentListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Department items for given requested user
        '''
        departments = Department.objects
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Department with given department data
        '''
        data = {
            'name': request.data.get('name'),
            'content': request.data.get('content'),
            'institute': request.data.get('institute'),
        }
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, department_id):
        '''
        Helper method to get the object with given department_id
        '''
        try:
            return Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, department_id, *args, **kwargs):
        '''
        Retrieves the Department with given department_id
        '''
        department_instance = self.get_object(department_id)
        if not department_instance:
            return Response(
                {"res": "Object with department id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DepartmentSerializer(department_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, department_id, *args, **kwargs):
        '''
        Updates the department item with given department_id if exists
        '''
        department_instance = self.get_object(department_id)
        if not department_instance:
            return Response(
                {"res": "Object with department id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'content': request.data.get('content'),
            'institute': request.data.get('institute'),
        }
        serializer = DepartmentSerializer(instance=department_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, department_id, *args, **kwargs):
        '''
        Deletes the department item with given department_id if exists
        '''
        department_instance = self.get_object(department_id)
        if not department_instance:
            return Response(
                {"res": "Object with department id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        department_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class SpecializationListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Specialization items for given requested user
        '''
        specializations = Specialization.objects
        serializer = SpecializationSerializer(specializations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Specialization with given specialization data
        '''
        data = {
            'name': request.data.get('name'),
            'number_specialization': request.data.get('number_specialization'),
            'content': request.data.get('content'),
            'department': request.data.get('department'),
        }
        serializer = SpecializationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecializationDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, specialization_id):
        '''
        Helper method to get the object with given specialization_id
        '''
        try:
            return Specialization.objects.get(id=specialization_id)
        except Specialization.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, specialization_id, *args, **kwargs):
        '''
        Retrieves the Specialization with given specialization_id
        '''
        specialization_instance = self.get_object(specialization_id)
        if not specialization_instance:
            return Response(
                {"res": "Object with specialization id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SpecializationSerializer(specialization_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, specialization_id, *args, **kwargs):
        '''
        Updates the specialization item with given specialization_id if exists
        '''
        specialization_instance = self.get_object(specialization_id)
        if not specialization_instance:
            return Response(
                {"res": "Object with specialization id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'number_specialization': request.data.get('number_specialization'),
            'content': request.data.get('content'),
            'department': request.data.get('department'),
        }
        serializer = SpecializationSerializer(instance=specialization_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, specialization_id, *args, **kwargs):
        '''
        Deletes the specialization item with given specialization_id if exists
        '''
        specialization_instance = self.get_object(specialization_id)
        if not specialization_instance:
            return Response(
                {"res": "Object with specialization id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        specialization_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class GroupListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Group items for given requested user
        '''
        groups = Group.objects
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the group with given group data
        '''
        data = {
            'name': request.data.get('name'),
            'specialization': request.data.get('specialization')
        }
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, group_id):
        '''
        Helper method to get the object with given group_id
        '''
        try:
            return Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, group_id, *args, **kwargs):
        '''
        Retrieves the Group with given group_id
        '''
        group_instance = self.get_object(group_id)
        if not group_instance:
            return Response(
                {"res": "Object with group id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = GroupSerializer(group_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, group_id, *args, **kwargs):
        '''
        Updates the group item with given group_id if exists
        '''
        group_instance = self.get_object(group_id)
        if not group_instance:
            return Response(
                {"res": "Object with group id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'specialization': request.data.get('specialization')
        }
        serializer = GroupSerializer(instance=group_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, group_id, *args, **kwargs):
        '''
        Deletes the group item with given group_id if exists
        '''
        group_instance = self.get_object(group_id)
        if not group_instance:
            return Response(
                {"res": "Object with group id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        group_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class StudentListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Student items for given requested user
        '''
        students = Student.objects
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the student with given student data
        '''
        data = {
            'login': request.data.get('login'),
            'password': request.data.get('password'),
            'name': request.data.get('name'),
            'surname': request.data.get('surname'),
            'patronymic': request.data.get('patronymic'),
            'pas_data': request.data.get('pas_data'),
            'telephone': request.data.get('telephone'),
            'email': request.data.get('email'),
            'group': request.data.get('group'),
        }
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, student_id):
        '''
        Helper method to get the object with given student_id
        '''
        try:
            return Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, student_id, *args, **kwargs):
        '''
        Retrieves the Student with given student_id
        '''
        student_instance = self.get_object(student_id)
        if not student_instance:
            return Response(
                {"res": "Object with student id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = StudentSerializer(student_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, student_id, *args, **kwargs):
        '''
        Updates the student item with given student_id if exists
        '''
        student_instance = self.get_object(student_id)
        if not student_instance:
            return Response(
                {"res": "Object with student id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'login': request.data.get('login'),
            'password': request.data.get('password'),
            'name': request.data.get('name'),
            'surname': request.data.get('surname'),
            'patronymic': request.data.get('patronymic'),
            'pas_data': request.data.get('pas_data'),
            'telephone': request.data.get('telephone'),
            'email': request.data.get('email'),
            'group': request.data.get('group'),
        }
        serializer = StudentSerializer(instance=student_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, student_id, *args, **kwargs):
        '''
        Deletes the student item with given student_id if exists
        '''
        student_instance = self.get_object(student_id)
        if not student_instance:
            return Response(
                {"res": "Object with student id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        student_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class SubjectListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Subject items for given requested user
        '''
        subjects = Subject.objects
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the subject with given subject data
        '''
        data = {
            'name': request.data.get('name'),
            'specialization': request.data.get('specialization'),
        }
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, subject_id):
        '''
        Helper method to get the object with given subject_id
        '''
        try:
            return Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, subject_id, *args, **kwargs):
        '''
        Retrieves the Subject with given subject_id
        '''
        subject_instance = self.get_object(subject_id)
        if not subject_instance:
            return Response(
                {"res": "Object with subject id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SubjectSerializer(subject_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, subject_id, *args, **kwargs):
        '''
        Updates the subject item with given subject_id if exists
        '''
        subject_instance = self.get_object(subject_id)
        if not subject_instance:
            return Response(
                {"res": "Object with subject id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'specialization': request.data.get('specialization'),
        }
        serializer = SubjectSerializer(instance=subject_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, subject_id, *args, **kwargs):
        '''
        Deletes the exam item with given exam_id if exists
        '''
        exam_instance = self.get_object(subject_id)
        if not exam_instance:
            return Response(
                {"res": "Object with exam id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        exam_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class ExamListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Exam items for given requested user
        '''
        exams = Exam.objects
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the exam with given exam data
        '''
        data = {
            'date_time_of_exam': request.data.get('date_time_of_exam'),
            'grading': request.data.get('grading'),
            'student': request.data.get('student'),
            'subject': request.data.get('subject'),
        }
        serializer = ExamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, exam_id):
        '''
        Helper method to get the object with given exam_id
        '''
        try:
            return Exam.objects.get(id=exam_id)
        except Exam.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, exam_id, *args, **kwargs):
        '''
        Retrieves the Exam with given exam_id
        '''
        exam_instance = self.get_object(exam_id)
        if not exam_instance:
            return Response(
                {"res": "Object with exam id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ExamSerializer(exam_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, exam_id, *args, **kwargs):
        '''
        Updates the exam item with given exam_id if exists
        '''
        exam_instance = self.get_object(exam_id)
        if not exam_instance:
            return Response(
                {"res": "Object with exam id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'date_time_of_exam': request.data.get('date_time_of_exam'),
            'grading': request.data.get('grading'),
            'student': request.data.get('student'),
            'subject': request.data.get('subject'),
        }
        serializer = ExamSerializer(instance=exam_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, exam_id, *args, **kwargs):
        '''
        Deletes the exam item with given exam_id if exists
        '''
        exam_instance = self.get_object(exam_id)
        if not exam_instance:
            return Response(
                {"res": "Object with exam id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        exam_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class EmployeeListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Employee items for given requested user
        '''
        employees = Employee.objects
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the employee with given employee data
        '''
        data = {
            'login': request.data.get('login'),
            'password': request.data.get('password'),
            'name': request.data.get('name'),
            'surname': request.data.get('surname'),
            'patronymic': request.data.get('patronymic'),
            'pas_data': request.data.get('pas_data'),
            'telephone': request.data.get('telephone'),
            'email': request.data.get('email'),
            'department': request.data.get('department'),
        }
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, employee_id):
        '''
        Helper method to get the object with given employee_id
        '''
        try:
            return Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, employee_id, *args, **kwargs):
        '''
        Retrieves the Employee with given employee_id
        '''
        employee_instance = self.get_object(employee_id)
        if not employee_instance:
            return Response(
                {"res": "Object with employee id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmployeeSerializer(employee_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, employee_id, *args, **kwargs):
        '''
        Updates the employee item with given employee_id if exists
        '''
        employee_instance = self.get_object(employee_id)
        if not employee_instance:
            return Response(
                {"res": "Object with employee id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'login': request.data.get('login'),
            'password': request.data.get('password'),
            'name': request.data.get('name'),
            'surname': request.data.get('surname'),
            'patronymic': request.data.get('patronymic'),
            'pas_data': request.data.get('pas_data'),
            'telephone': request.data.get('telephone'),
            'email': request.data.get('email'),
            'department': request.data.get('department'),
        }
        serializer = EmployeeSerializer(instance=employee_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, employee_id, *args, **kwargs):
        '''
        Deletes the employee item with given employee_id if exists
        '''
        employee_instance = self.get_object(employee_id)
        if not employee_instance:
            return Response(
                {"res": "Object with employee id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        employee_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class LessonListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Lesson items for given requested user
        '''
        lessons = Lesson.objects
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the lesson with given lesson data
        '''
        data = {
            'number': request.data.get('number'),
            'time_start': request.data.get('time_start'),
            'time_end': request.data.get('time_end'),
        }
        serializer = LessonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, lesson_id):
        '''
        Helper method to get the object with given lesson_id
        '''
        try:
            return Lesson.objects.get(id=lesson_id)
        except Lesson.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, lesson_id, *args, **kwargs):
        '''
        Retrieves the Lesson with given lesson_id
        '''
        lesson_instance = self.get_object(lesson_id)
        if not lesson_instance:
            return Response(
                {"res": "Object with lesson id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LessonSerializer(lesson_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, lesson_id, *args, **kwargs):
        '''
        Updates the lesson item with given lesson_id if exists
        '''
        lesson_instance = self.get_object(lesson_id)
        if not lesson_instance:
            return Response(
                {"res": "Object with lesson id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'number': request.data.get('number'),
            'time_start': request.data.get('time_start'),
            'time_end': request.data.get('time_end'),
        }
        serializer = LessonSerializer(instance=lesson_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, lesson_id, *args, **kwargs):
        '''
        Deletes the lesson item with given lesson_id if exists
        '''
        lesson_instance = self.get_object(lesson_id)
        if not lesson_instance:
            return Response(
                {"res": "Object with lesson id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        lesson_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class Classes_SheldueListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Classes_Sheldue items for given requested user
        '''
        classes_Sheldues = Classes_Sheldue.objects
        serializer = Classes_SheldueSerializer(classes_Sheldues, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the classes_Sheldue with given classes_Sheldue data
        '''
        data = {
            'classroom': request.data.get('classroom'),
            'day_of_the_week': request.data.get('day_of_the_week'),
            'group': request.data.get('group'),
            'subject': request.data.get('subject'),
            'employee': request.data.get('employee'),
            'lesson': request.data.get('lesson'),
        }
        serializer = Classes_SheldueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Classes_SheldueDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, classes_sheldue_id):
        '''
        Helper method to get the object with given classes_sheldue_id
        '''
        try:
            return Classes_Sheldue.objects.get(id=classes_sheldue_id)
        except Classes_Sheldue.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, classes_sheldue_id, *args, **kwargs):
        '''
        Retrieves the Classes_Sheldue with given classes_sheldue_id
        '''
        classes_Sheldue_instance = self.get_object(classes_sheldue_id)
        if not classes_Sheldue_instance:
            return Response(
                {"res": "Object with classes_Sheldue id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = Classes_SheldueSerializer(classes_Sheldue_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, classes_sheldue_id, *args, **kwargs):
        '''
        Updates the classes_Sheldue item with given classes_sheldue_id if exists
        '''
        classes_Sheldue_instance = self.get_object(classes_sheldue_id)
        if not classes_Sheldue_instance:
            return Response(
                {"res": "Object with classes_Sheldue id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'classroom': request.data.get('classroom'),
            'day_of_the_week': request.data.get('day_of_the_week'),
            'group': request.data.get('group'),
            'subject': request.data.get('subject'),
            'employee': request.data.get('employee'),
            'lesson': request.data.get('lesson'),
        }
        serializer = Classes_SheldueSerializer(instance=classes_Sheldue_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, classes_sheldue_id, *args, **kwargs):
        '''
        Deletes the classes_Sheldue item with given classes_sheldue_id if exists
        '''
        classes_Sheldue_instance = self.get_object(classes_sheldue_id)
        if not classes_Sheldue_instance:
            return Response(
                {"res": "Object with classes_Sheldue id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        classes_Sheldue_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
