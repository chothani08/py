from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", formatted_time)