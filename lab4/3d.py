from datetime import datetime

# Create a datetime object with microseconds
current_datetime = datetime.now()

# Drop microseconds
datetime_without_microseconds = current_datetime.replace(microsecond=0)

# Print the results
print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)
