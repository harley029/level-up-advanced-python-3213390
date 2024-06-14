# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
from datetime import datetime, timedelta

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhines_times = []
    ptrn = r"\d{2}:\S+"
    for line in races.splitlines():
        if 'Jennifer Rhines' in line:
           rhines_times.append(re.findall(ptrn, line)[0])
    return rhines_times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = timedelta()
    for racetime in racetimes:
        if len(racetime) == 5:
            t = datetime.strptime(racetime, "%M:%S")
            rase_delta = timedelta(minutes=t.minute, seconds=t.second)
        else:
            t = datetime.strptime(racetime, "%M:%S.%f")
            rase_delta = timedelta(
                minutes=t.minute, 
                seconds=t.second,
                microseconds=t.microsecond)
        total += rase_delta
    # print(total/len(racetimes))
    return f'{total / len(racetimes)}'[2:-5]