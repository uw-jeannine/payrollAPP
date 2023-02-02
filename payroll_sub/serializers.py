from rest_framework import serializers
from .models import *

class Fetchserializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"

class Getserializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"