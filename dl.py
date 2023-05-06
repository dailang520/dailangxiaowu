import time

def pomodoro_timer(minutes):
    '''
    This function creates a Pomodoro timer for a specified number of minutes.
    It will display a countdown and a message when the time is up.
    '''
    seconds = minutes * 60

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_display, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up! Take a break.")

# 使用示例
pomodoro_timer(25) # 25分钟专注计时器
