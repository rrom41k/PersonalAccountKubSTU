from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import (Institute, Department, Specialization, Group, Student, Subject, Exam, Employee, Lesson,
                     Classes_Sheldue)
from .serializers import (InstituteSerializer, DepartmentSerializer, SpecializationSerializer,  GroupSerializer,
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
            'content': request.data.get('specialization')
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
