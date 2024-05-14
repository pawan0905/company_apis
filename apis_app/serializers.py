from .models import*
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"