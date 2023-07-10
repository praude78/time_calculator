def add_time(start_time, duration, start_day=None):
    # Parse the start time
    start_time_hour, start_time_minute = map(int, start_time.split(":"))
    start_time_period = start_time.split()[-1]  # AM or PM
