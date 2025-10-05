def add_time(start, duration, day=''):
    # Parse start time
    start_parts = start.split()
    time_str = start_parts[0]
    period = start_parts[1]
    h, m = map(int, time_str.split(':'))
    
    # Convert start to 24-hour format
    if period == 'PM' and h != 12:
        start_h = h + 12
    elif period == 'AM' and h == 12:
        start_h = 0
    else:
        start_h = h
    
    start_min = start_h * 60 + m
    
    # Parse duration
    dur_parts = duration.split(':')
    dur_h = int(dur_parts[0])
    dur_m = int(dur_parts[1])
    
    add_min = dur_h * 60 + dur_m
    
    # Calculate new time
    new_min = start_min + add_min
    days_added = new_min // 1440
    new_min %= 1440
    
    new_h24 = new_min // 60
    new_m_val = new_min % 60
    
    # Convert to 12-hour format
    if new_h24 == 0:
        new_h12 = 12
        new_p = 'AM'
    elif new_h24 == 12:
        new_h12 = 12
        new_p = 'PM'
    elif new_h24 > 12:
        new_h12 = new_h24 - 12
        new_p = 'PM'
    else:
        new_h12 = new_h24
        new_p = 'AM'
    
    time_str_new = f"{new_h12}:{new_m_val:02d} {new_p}"
    
    # Determine extra string for days
    if days_added == 0:
        extra = ""
    elif days_added == 1:
        extra = " (next day)"
    else:
        extra = f" ({days_added} days later)"
    
    # Handle day of the week if provided
    if day:
        days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_lower = day.lower()
        day_index = days_list.index(day_lower)
        new_day_index = (day_index + days_added) % 7
        new_day = days_list[new_day_index].title()
        
        if extra:
            result = f"{time_str_new}, {new_day}{extra}"
        else:
            result = f"{time_str_new}, {new_day}"
    else:
        if extra:
            result = f"{time_str_new}{extra}"
        else:
            result = time_str_new
    
    return result