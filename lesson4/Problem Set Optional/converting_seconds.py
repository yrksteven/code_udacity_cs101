# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(seconds):
    hour = int(seconds / 3600)
    minute = int((seconds - hour * 3600) / 60)
    second = seconds - hour * 3600 - minute * 60
    a, b, c = ' hour', ' minute', ' second'
    if hour > 1 or hour ==0:
        a = ' hours'
    if minute > 1 or minute == 0:
        b = ' minutes'
    if second > 1 or second == 0:
        c = ' seconds'
    return str(hour) + a + ', ' + str(minute) + b + ', ' + str(second) + c

print convert_seconds(60)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds