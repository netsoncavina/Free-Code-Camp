def add_time(start, duration, startDay = False):
    # Start values
    start_hour = start.split(':')[0]
    start_minute = start.split(' ')[0].split(':')[1]
    start_period = start.split(' ')[1]

    # Duration values
    duration_hour = duration.split(':')[0]
    duration_minute = duration.split(':')[1]

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Calculate the new time
    new_hour = int(start_hour) + int(duration_hour)
    new_minute = int(start_minute) + int(duration_minute)
    if new_minute >= 60:
        new_minute -= 60
        new_hour += 1
    
    # Check if the new time is at 12:00
    new_hour = new_hour % 24
    if start_period == "AM":
        if new_hour == 12:
            new_period = "PM"
        elif new_hour >= 12:
            new_hour -= 12
            new_period = "PM"
        else:
            new_period = "AM"
    else:
        if new_hour == 12:
            new_period = "AM"
        elif new_hour >= 12:
            new_hour -= 12
            new_period = "AM"
        else:
            new_period = "PM"
    if new_hour == 0:
        new_hour = 12

    #  Calculate the new day
    if startDay:
        startDay = startDay.capitalize()
        new_day = days[(days.index(startDay) + int(duration_hour)) % 7]
        print(f"{new_hour}:{new_minute:02d} {new_period}, {new_day}")
    else:
        new_day = startDay
        print(f"{new_hour:02d}:{new_minute:02d} {new_period}")
    # return new_time
    
# add_time("8:16 PM", "466:02")
# add_time("5:01 AM", "0:00")
add_time("2:59 AM", "24:00", "Saturday")
add_time("11:59 PM", "24:05", "Wednesday")