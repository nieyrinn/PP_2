from datetime import datetime, timedelta

# Get user input for the date
user_input = input()

# Convert the user input to a datetime object
try:
    user_date = datetime.strptime(user_input, "%Y-%m-%d")
except ValueError:
    print()
    exit()

# Subtract five days
new_date = user_date - timedelta(days=5)

# Print the result
print("Entered Date:", user_date.strftime("%Y-%m-%d"))
print("Date after subtracting five days:", new_date.strftime("%Y-%m-%d"))
