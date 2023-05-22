from plyer import notification
import datetime

# Set the alarm to 6 PM
alarm_time = datetime.datetime.now().replace(
    hour=18, minute=0, second=0, microsecond=0)

# Calculate the remaining time until the alarm goes off
remaining_time = alarm_time - datetime.datetime.now()


# Convert the remaining time to seconds
remaining_time_seconds = remaining_time.total_seconds()


# Set up the notification message
if remaining_time_seconds > 0:
    message = "Do your best. Only " + \
        str(int(remaining_time_seconds/60)) + " minutes remaining."
else:
    message = "You can stop working at any time now."


# Set up the notification
notification.notify(title='Work Reminder',
                    message=message,
                    timeout=10  # The notification will be displayed for 10 seconds
                    )
