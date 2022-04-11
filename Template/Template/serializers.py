from rest_framework import serializers

class SearchSerializer(serializers.ModelSerializer):
    keyword = serializers.CharField(max_length=255, label="Search Here")
    # created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    # updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
