from datetime import datetime

now = datetime.now()
print(f"Current date and time: {now}")

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_now}")
