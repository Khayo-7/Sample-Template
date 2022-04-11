from rest_framework import serializers
from incidents.models import *

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

# class SearchSerializer(serializers.ModelSerializer):
#     key = serializers.CharField(max_length=255, label="Search Here")

#     # created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
#     # updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")

#     class Meta:
#         fields = '__all__'
