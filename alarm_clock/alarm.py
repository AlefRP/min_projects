from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour, alarm_minute, alarm_seconds = alarm_time.split(":")

while True:
    now = datetime.now()
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")

    if alarm_hour == current_hour and alarm_minute == current_minute and alarm_seconds == current_seconds:
        print("Wake up!")
        playsound('alarm_clock\\audio\\alarm-clock.mp3')
        break