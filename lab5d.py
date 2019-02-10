class Time(object):
    """Time of day.attributes: hour, minute, second"""

t1 = Time()
t1.hour = 11
t1.minute = 59
t1.second = 30

t2 = Time()
t2.hour = 10
t2.minute = 45
t2.second = 25

def is_after(t1, t2):
    t1_total_seconds = (t1.hour * 3600) + (t1.minute * 60) + t1.second
    t2_total_seconds = (t2.hour * 3600) + (t2.minute * 60) + t2.second
    return t1_total_seconds > t2_total_seconds

print(is_after(t1, t2))
