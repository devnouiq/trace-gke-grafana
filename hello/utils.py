from hello.decorators import trace_function
from django.db import connection
import time

# @trace_function()
def perform_computation():
    result = {"value": 42}
    return result

# @trace_function()
def fetch_from_database():
    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello from the database!' as message")
    result = cursor.fetchone()
    return result[0]

# @trace_function()
def save_time_to_db(current_time):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS time_log (id INTEGER PRIMARY KEY, timestamp TEXT)")
    cursor.execute("INSERT INTO time_log (timestamp) VALUES (%s)", [current_time])
    connection.commit()

# @trace_function(span_name="simulate-timeout")
def simulate_timeout():
    time.sleep(5)  # Simulating a timeout
    raise Exception("Simulated timeout occurred")

# @trace_function(span_name="simulate-db-error")
def simulate_database_error():
    raise Exception("Simulated database connection error")
