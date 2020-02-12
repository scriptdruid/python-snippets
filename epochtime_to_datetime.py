import datetime
from pytz import timezone

start_date = 1537774710
d2 = 1525054027

datetime.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d %H:%M:%S')
datetime.datetime.fromtimestamp(d2).strftime('%Y-%m-%d %H:%M:%S')
datetime.datetime.utcfromtimestamp(d2).strftime('%Y-%m-%d %H:%M:%S')

ts_date = datetime.datetime.fromtimestamp(
    start_date).strftime('%b/%d/%Y %H:%M:%S')

datetime.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d %H:%M:%S')

d_time = datetime.datetime.fromtimestamp(d2)


def parse_date_param(date_str):
    """Parse a date of the form Mmm/dd/yyyy where Mmm is the short form of
    month like Jan, Feb etc.
    """
    return datetime.datetime.strptime(date_str, '%b/%d/%Y')


parse_date_param("apr/30/2018")

day_start_time = d_time.hour * 60 + d_time.minute


def parse_date_param_n(date_str):
    """Parse a date of the form Mmm/dd/yyyy where Mmm is the short form of
    month like Jan, Feb etc.
    """
    parsed_date = datetime.datetime.fromtimestamp(date_str)
    minutes = parsed_date.hour * 60 + parsed_date.minute
    return parsed_date, minutes


print(parse_date_param_n(d2))

print(parse_date_param_n(1537774710))
