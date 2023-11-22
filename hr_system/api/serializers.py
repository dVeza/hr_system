from rest_framework import serializers

from hr_system.entities.models import Employee, Industry


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class IndustrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"
