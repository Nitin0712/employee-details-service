from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# from rest_framework.views import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Employee
from .serializers import EmployeeSerializer


class employeeList(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer = EmployeeSerializer

#
# class employeeDetail(viewsets.ModelViewSet):
#     queryset = Employee.objects.get(id=id)
#     serializer = EmployeeSerializer
