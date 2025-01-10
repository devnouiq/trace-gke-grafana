from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter as OTLPHTTPSpanExporter
from opentelemetry.trace import set_tracer_provider

def setup_tracing(endpoint):
    """
    Initialize OpenTelemetry tracing with the specified endpoint.
    """
    resource = Resource(attributes={
        "service.name": "django-helloworld",
        "environment": "local",  # Customize for staging, production, etc.
    })

    # Initialize TracerProvider
    tracer_provider = TracerProvider(resource=resource)
    set_tracer_provider(tracer_provider)

    # Add a BatchSpanProcessor with the OTLP HTTP exporter
    span_processor = BatchSpanProcessor(OTLPHTTPSpanExporter(endpoint=endpoint))
    tracer_provider.add_span_processor(span_processor)

    # Instrument Django
    DjangoInstrumentor().instrument()
