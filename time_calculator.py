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
    
    # Determine the period (AM or PM) and adjust the hour
    if end_time_hour < 12:
        end_time_period = "AM"
    else:
        end_time_period = "PM"
        if end_time_hour > 12:
            end_time_hour -= 12
            
    # Determine the number of days later
    days_later = (start_time_hour + duration_hour + carry_hour) // 24
    
    # Determine the day of the week
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if start_day:
        start_day = start_day.lower().capitalize()
        start_day_index = days_of_week.index(start_day)
        end_day_index = (start_day_index + days_later) % 7
        end_day = days_of_week[end_day_index]



