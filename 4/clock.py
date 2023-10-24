'''
  display all the minutes from 0:00
  until the user specified time HH:MM (i.e. 3:15)
'''

# collect time from user
end = input("enter end time: ")
end_time = end.split(":") # ["HH","MM"]
end_hour = int(end_time[0])
end_mins = int(end_time[1])

# initialize time 0:00

# count
for hour in range(24):      # [0,1,2,...,23]
    for mins in range(60):  # [0,1,2,...,59]
        print(hour,":",mins)
        if (hour == end_hour and mins == end_mins):
            break
    if (hour == end_hour):
        break
print("all done!")
