from json import loads

import pandas as pd
from django.db.models import F, Func, IntegerField, Value
from django.utils import timezone
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from hr_system.api.serializers import EmployeeSerializer, IndustrySerializer
from hr_system.entities.models import Employee, Industry


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """

    queryset = Employee.objects.all().order_by("-created_at")
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndustryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows industries to be viewed or edited.
    """

    queryset = Industry.objects.all().order_by("-created_at")
    serializer_class = IndustrySerializer
    permission_classes = [permissions.IsAuthenticated]


class StatsViewSet(viewsets.ViewSet):
    """
    Compute stats using pandas
    """

    def list(self, request, format=None):
        queryset = Employee.objects.all()
        queryset = queryset.annotate(
            age=Func(
                Value("year"),
                Func(Value(timezone.now().date()), F("date_of_birth"), function="age"),
                function="date_part",
                output_field=IntegerField(),
            ),
        ).select_related("industry")

        if industry_id := request.GET.get("industry_id"):
            queryset = queryset.filter(industry__id=industry_id)
        if gender := request.GET.get("gender"):
            queryset = queryset.filter(gender=gender)

        if not queryset.exists():
            return Response("No data")

        queryset = queryset.values_list("salary", "years_experience", "age")
        df = pd.DataFrame(list(queryset), columns=["salary", "years_experience", "age"])
        df2 = df.mean(axis=0)

        data = {
            "average_salary": round(df2["salary"], 2),
            "average_experience": round(df2["years_experience"], 2),
            "average_age": round(df2["age"], 2),
        }

        return Response(data)


class StatsViewSetV2(viewsets.ViewSet):
    """
    Compute stats using pandas
    """

    def list(self, request, format=None):
        queryset = Employee.objects.all()
        queryset = queryset.annotate(
            age=Func(
                Value("year"),
                Func(Value(timezone.now().date()), F("date_of_birth"), function="age"),
                function="date_part",
                output_field=IntegerField(),
            ),
        ).select_related("industry")

        if industry_id := request.GET.get("industry_id"):
            queryset = queryset.filter(industry__id=industry_id)
        if gender := request.GET.get("gender"):
            queryset = queryset.filter(gender=gender)

        if not queryset.exists():
            return Response("No data")

        queryset = queryset.values_list(
            "industry__name", "salary", "years_experience", "age"
        )
        df = pd.DataFrame(
            list(queryset), columns=["industry", "salary", "years_experience", "age"]
        )
        df2 = df.groupby(["industry"]).mean()

        data = {}
        for industry, average_salary, avg_experience, avg_age in df2.itertuples():
            data[industry] = {
                "average_salary": round(average_salary, 2),
                "average_experience": round(avg_experience, 2),
                "average_age": round(avg_age, 2),
            }

        return Response(data)
