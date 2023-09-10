from rest_framework import serializers

class Datetimeserializer(serializers.Serializer):
    slack_name = serializers.CharField()
    current_day = serializers.DateField()
    utc_time = serializers.DateTimeField(format="2023-09-09T%H:%M:%SZ")
    track = serializers.CharField()
    github_file_url = serializers.CharField() 
    github_repo_url = serializers.CharField() 
    status_code = serializers.IntegerField()
