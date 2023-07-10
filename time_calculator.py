def add_time(start_time, duration, start_day=None):
    # Parse the start time
    start_time_hour, start_time_minute = map(int, start_time.split(":"))
    start_time_period = start_time.split()[-1]  # AM or PM
    
    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Convert start time to 24-hour format
    if start_time_period == "PM":
        start_time_hour += 12

    # Add the duration time
    end_time_minute = (start_time_minute + duration_minute) % 60
    carry_hour = (start_time_minute + duration_minute) // 60
    end_time_hour = (start_time_hour + duration_hour + carry_hour) % 24
