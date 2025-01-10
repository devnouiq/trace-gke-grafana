from django.http import JsonResponse
from datetime import datetime
from hello.utils import save_time_to_db, perform_computation, fetch_from_database
from hello.decorators import trace_function

@trace_function()
def hello_world(request):
    result = perform_computation()
    data = fetch_from_database()
    return JsonResponse({"message": "Hello, World!", "result": result, "data": data})

@trace_function()
def time_route(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    save_time_to_db(current_time)
    return JsonResponse({"time": current_time})
