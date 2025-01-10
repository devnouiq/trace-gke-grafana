from functools import wraps
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def trace_function(span_name=None):
    """
    Decorator to trace a function.
    If span_name is not provided, it defaults to the function name.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use the function name as the span name if none is provided
            current_span_name = span_name or func.__name__
            with tracer.start_as_current_span(current_span_name) as span:
                trace_id = span.get_span_context().trace_id
                print(f"Trace ID for {current_span_name}: {trace_id}")  # Log Trace ID
                return func(*args, **kwargs)
        return wrapper
    return decorator
