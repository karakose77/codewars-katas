# HUMAN READABLE TIME
#
# Write a function, which takes a non-negative integer (seconds) as input and
# returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.


def make_readable(seconds):
    time_list = [0, 0, 0]
    time_str = ""
    time_list[2] = seconds
    if time_list[2] > 359999:
        time_list[2] = 359999
    time_list[0] = time_list[2] // 3600
    time_list[2] = time_list[2] % 3600
    time_list[1] = time_list[2] // 60
    time_list[2] = time_list[2] % 60
    for item in time_list:
        item_str = str(item)
        if len(item_str) == 1:
            time_str += "0" + item_str
        else:
            time_str += item_str
        time_str += ":"
    time_str = time_str[:-1]
    return time_str


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
print(make_readable(366999))
