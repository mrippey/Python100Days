from datetime import datetime, timedelta 
import time 
import sys

def my_pomodoro_like_timer():
    timer_setup = int(input('How long? '))
    if timer_setup < 0:
        timeError = ValueError('Number of minutes should be positive')
        raise timeError
    start = str(input('Ready to start timer (Y/N)? '))
    if start != 'Y':
        sys.exit()
    else:
        now = datetime.now()
        end = now + timedelta(minutes=timer_setup)
        print(f'Timer starting now at {now}, end time: {end}')
        time.sleep(timer_setup * 60)
        end_time = end.strftime('%H:%M:%S')
        print(f'Times Up!!!, Current time is: {end_time}')
        

my_pomodoro_like_timer()
