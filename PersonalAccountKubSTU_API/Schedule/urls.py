from django.urls import path, include
from .views import (
    InstituteListApiView,
    InstituteDetailApiView,
    DepartmentListApiView,
    DepartmentDetailApiView,
    GroupListApiView,
    GroupDetailApiView
)

urlpatterns = [
    path('api/institute/', InstituteListApiView.as_view()),
    path('api/institute/<int:group_id>/', InstituteDetailApiView.as_view()),

    path('api/department/', DepartmentListApiView.as_view()),
    path('api/department/<int:group_id>/', DepartmentDetailApiView.as_view()),

    path('api/group/', GroupListApiView.as_view()),
    path('api/group/<int:group_id>/', GroupDetailApiView.as_view()),
]
