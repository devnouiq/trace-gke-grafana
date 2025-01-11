import os
from django.core.wsgi import get_wsgi_application
from helloworld.otel_config import setup_tracing
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Tempo endpoint from the environment
otel_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld.settings')

# Initialize OpenTelemetry tracing
setup_tracing(endpoint=otel_endpoint)

# Set up the WSGI application
application = get_wsgi_application()
