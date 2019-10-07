# https://www.codewars.com/kata/human-readable-duration-format/train/python


# import datetime
from datetime import datetime as dt
import dateutil.relativedelta as ut


def format_duration(seconds):
    if seconds == 0:
        return 'Now'

    # Calculate Duration
    x = dt.fromtimestamp(0)
    y = dt.fromtimestamp(seconds)
    r = ut.relativedelta(y, x)

    # Duration Parts
    y = r.years
    d = r.days
    h = r.hours
    m = r.minutes
    s = r.seconds

    # Time String Parts (For Singular vs Plural Output)
    year = [y, f'{y} years', f'{y} year']
    day = [d, f'{d} days', f'{d} day']
    hour = [h, f'{h} hours', f'{h} hour']
    minute = [m, f'{m} minutes', f'{m} minute']
    second = [s, f'{s} seconds', f'{s} second']

    # Time String Parts List
    parts = [year, day, hour, minute, second]

    # Define Duration List of Parts
    duration = []

    # Put durations together
    for part in parts:
        if part[0] and part[0] > 1:
            duration.append(part[1])
        elif part[0] and part[0] == 1:
            duration.append(part[2])

    # Add an 'and' if needed
    if len(duration) > 1:
        duration.insert(-1, 'and')

    print(' '.join(duration))
    return ' '.join(duration)


format_duration(38473728)


'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
Detailed rules

The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''

'''
test.assert_equals(format_duration(1), "1 second")
test.assert_equals(format_duration(62), "1 minute and 2 seconds")
test.assert_equals(format_duration(120), "2 minutes")
test.assert_equals(format_duration(3600), "1 hour")
test.assert_equals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
'''
