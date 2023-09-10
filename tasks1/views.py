from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Datetimeserializer
from datetime import datetime
from django.http import JsonResponse


def CustomAPI(request):
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%SZ")
    response_data={
        'current_date':formatted_date,
        'current_time': formatted_time
    }

    return JsonResponse(response_data)


class CustomAPI(APIView):
    def get(self, request):
        param_value = request.query_params.get("slack_name=olamilekan1&track=backend")
        current_datetime = datetime.now()
        current = Datetimeserializer({
             "slack_name": "olamilekan1", 
             "current_day":"Saturday",
             "utc_time": current_datetime.time(),
             "track": "backend", 
             "github_file_url": "https://github.com/lekan2/taskK-/tree/main/tasks1", 
             "github_repo_url": "https://github.com/lekan2/task.git", 
             "status_code": 200
            }).data

   
        return Response(current)
