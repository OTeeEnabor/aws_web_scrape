from datetime import datetime
# get current time

# Get current date and time
now = datetime.now()

# Format to get only time
current_time = now.strftime("%A, %B %d, %Y, %I %p %Z")


with open("cron_test.txt", "a") as file:
    file.write(f"Current Date and time :{now} \n")