import datetime

def log_uptime():
    current_time = datetime.datetime.now()
    uptime_since_epoch = (current_time - datetime.datetime(1970, 1, 1)).total_seconds()
    with open('uptime_log.txt', 'a') as file:
        file.write(f'Uptime at {current_time}: {uptime_since_epoch} seconds\n')

log_uptime()