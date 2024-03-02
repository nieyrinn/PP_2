from datetime import datetime, timedelta

# Get user input for the current date
date_str = input()
today = datetime.strptime(date_str, "%Y-%m-%d")

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday.s("%Y-%m-%d"))
print("Today:", today.s("%Y-%m-%d"))
print("Tomorrow:", tomorrow.s("%Y-%m-%d"))
