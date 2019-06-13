from rest_framework import serializers
from customers.models import Customer
from employees.models import Employee, EmployeePosition


class EmployeePositionSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField(many=False)

    class Meta:
        model = EmployeePosition
        fields = ('id', 'position', 'hour_rate')


class EmployeeSerializer(serializers.ModelSerializer):
    employeeposition_set = EmployeePositionSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'profile_image', 'first_name', 'last_name', 'email', 'hour_rate', 'employeeposition_set')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email')
