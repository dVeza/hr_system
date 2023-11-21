from hr_system.entities.models import Employee, Industry
from rest_framework import viewsets
from rest_framework import permissions
from hr_system.api.serializers import EmployeeSerializer, IndustrySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndustryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows industries to be viewed or edited.
    """
    queryset = Industry.objects.all().order_by('-created_at')
    serializer_class = IndustrySerializer
    permission_classes = [permissions.IsAuthenticated]
