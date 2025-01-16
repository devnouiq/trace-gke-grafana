from functools import wraps
from opentelemetry import trace
from opentelemetry.trace.status import Status, StatusCode
from django.http import JsonResponse
import json

tracer = trace.get_tracer(__name__)

def trace_function(span_name=None):
    """
    Decorator to trace a function or view.
    Automatically appends trace_id to JSON responses.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use the function name as the span name if none is provided
            current_span_name = span_name or func.__name__
            with tracer.start_as_current_span(current_span_name) as span:
                trace_id = span.get_span_context().trace_id
                try:
                    # Execute the original function
                    response = func(*args, **kwargs)
                    # Add trace ID to the response if it's a JsonResponse
                    if isinstance(response, JsonResponse):
                        response_data = json.loads(response.content)
                        response_data["trace_id"] = f"{trace_id:016x}"
                        response.content = json.dumps(response_data).encode("utf-8")
                    return response
                except Exception as e:
                    # Log the error and mark the span with an error status
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    raise e
        return wrapper
    return decorator
