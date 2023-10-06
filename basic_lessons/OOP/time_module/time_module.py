import time

print(time.ctime(0))  # convert a time expressed in seconds since epoch
# to a readable string. Epoch = when your computer thinks time began (reference point)
# 0 = moment of inicial time

print(time.time())  # return current seconds since epoch

print(time.ctime(time.time()))  # current time

time_object = time.localtime()  # gets my computer time
# time_object = time.gmtime()  # gets UTC time
print(time_object)
local_time = time.strftime("%d/%B/%Y %H:%M:%S", time_object)
print(local_time)

time_string = "20 April, 2020"
time_object2 = time.strptime(time_string, "%d %B, %Y")
print(time_object2)

# (Year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = 2020, 4, 20, 4, 20, 0, 0, 0, 0
time_string2 = time.asctime(time_tuple)
print(time_string2)

# (Year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = 2020, 4, 20, 4, 20, 0, 0, 0, 0
time_string2 = time.mktime(time_tuple)
print(time_string2)
