from rest_framework import viewsets
from.serializers import EmployeeSerializer
from.models import Employee
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated



class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]