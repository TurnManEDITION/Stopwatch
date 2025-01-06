def edit_data(local_data):
    if local_data[0] == "Mon": local_data[0] = "Monday"
    if local_data[0] == "Tue": local_data[0] = "Tuesday"
    if local_data[0] == "Wed": local_data[0] = "Wednesday"
    if local_data[0] == "Thu": local_data[0] = "Thursday"
    if local_data[0] == "Fri": local_data[0] = "Friday"
    if local_data[0] == "Sat": local_data[0] = "Saturday"
    if local_data[0] == "Sun": local_data[0] = "Sunday"

    if local_data[1] == "Dec": local_data[1] = "12"
    if local_data[1] == "Jan": local_data[1] = "01"
    if local_data[1] == "Feb": local_data[1] = "02"
    if local_data[1] == "Mar": local_data[1] = "03"
    if local_data[1] == "Apr": local_data[1] = "04"
    if local_data[1] == "May": local_data[1] = "05"
    if local_data[1] == "Jun": local_data[1] = "06"
    if local_data[1] == "Jul": local_data[1] = "07"
    if local_data[1] == "Aug": local_data[1] = "08"
    if local_data[1] == "Sep": local_data[1] = "09"
    if local_data[1] == "Oct": local_data[1] = "10"
    if local_data[1] == "Nov": local_data[1] = "11"

    if len(str(local_data[2])) == 1:
        local_data[2] = "0" + local_data[2]
    
    data = f"{local_data[2]}.{local_data[1]}.{local_data[4]}"
    local_data = [local_data[0], local_data[3], data]
    return local_data


def edit_stopwatch(times):
    hours = str(times[0])
    minutes = str(times[1])
    seconds = str(times[2])

    if len(hours) < 2:
        hours = "0" + hours
    if len(minutes) < 2:
        minutes = "0" + minutes
    if len(seconds) < 2:
        seconds = "0" + seconds

    times = f"{hours}:{minutes}:{seconds}"
    return times


def check_stopwatch(times):
    hours = int(times[0])
    minutes = int(times[1])
    seconds = int(times[2])

    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    times = [hours, minutes, seconds]
    return times


def work_stopwatch(times):
    hours = int(times[0])
    minutes = int(times[1])
    seconds = int(times[2])

    times = [hours, minutes, seconds + 1]
    return times


def start_edit_stopwatch(times):
    times = str(times).split(":")
    hours = int(times[0])
    minutes = int(times[1])
    seconds = int(times[2])

    if seconds > 60:
        minutes += seconds // 60
        seconds -= 60 * (seconds // 60)
    if minutes > 60:
        hours += minutes // 60
        minutes -= 60 * (minutes // 60)
    times = [hours, minutes, seconds]
    times = edit_stopwatch(times)
    return times
