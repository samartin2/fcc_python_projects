def add_time(start, duration, start_day=None):
  days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  time_arr = [0,0,0] # days, hours, minutes
  start_arr = start.split(" ")
  start_hour = int(start_arr[0].split(":")[0])
  start_min = int(start_arr[0].split(":")[1])
  dur_hour = int(duration.split(":")[0])
  dur_min = int(duration.split(":")[1])

  # Calculate the minutes
  mins = start_min + dur_min
  if mins > 59:
    time_arr[1] += 1
    time_arr[2] = mins - 60
  else:
    time_arr[2] = mins

  if time_arr[2] < 10:
    final_min = "0" + str(time_arr[2])
  else:
    final_min = str(time_arr[2])
  
  # Calculate the hours
  if start_arr[1] == "AM" and start_hour == 12:
    start_hour = 0
  elif start_arr[1] == "PM" and start_hour != 12:
    start_hour += 12

  total_hours = start_hour + dur_hour + time_arr[1]
  hours = total_hours % 24

  if hours > 12:
    am_pm = "PM"
    final_hours = str(hours - 12)
  elif hours == 12:
      am_pm = "PM"
      final_hours = str(hours)
  else:
    am_pm = "AM"
    if hours == 0:
      final_hours = "12"
    else:
      final_hours = str(hours)

  # Calculate the number of days
  total_days = total_hours // 24

  if total_hours > 24 + (24 - start_hour):
    final_days = str(total_days)
    final_days_str = " (" + final_days + " days later)"
  else:
    if total_days == 1:
      final_days_str = " (next day)"
    else:
      final_days_str = ""

  if start_day:
    days_mod = total_days % 7
    start_ind = next(i for i,v in enumerate(days) if v.lower() == start_day.lower())
    i = 0
    k = start_ind
    while i < days_mod:
      k = (k + 1) % len(days)
      i += 1
    final_day = days[k]
    new_time = final_hours + ":" + final_min + " " + am_pm + ", " + final_day + final_days_str

  else:
    new_time = final_hours + ":" + final_min + " " + am_pm + final_days_str

  return new_time