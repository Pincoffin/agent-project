import datetime

log_file = 'uptime_log.txt'

def log_uptime():
    current_time = datetime.datetime.now()
    uptime_since_epoch = (current_time - datetime.datetime(1970, 1, 1)).total_seconds()
    with open(log_file, 'a') as file:
        file.write(f'Uptime at {current_time}: {uptime_since_epoch} seconds\n')

if __name__ == '__main__':
    log_uptime()