from django.urls import include, path
from rest_framework import routers

from hr_system.api import views

router = routers.DefaultRouter()
router.register(r"employees", views.EmployeeViewSet, basename="employee")
router.register(r"industries", views.IndustryViewSet, basename="industry")
router.register(r"stats", views.StatsViewSet, basename="stats")
router.register(r"stats2", views.StatsViewSetV2, basename="stats2")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
