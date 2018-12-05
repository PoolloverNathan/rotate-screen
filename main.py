#!/usr/bin/env python3

# main: a program that flips the computer's screen(s) past a certain
# hour. See README.md for usage.
# Assumes the computer will be turned off during the night (i.e. doesn't get
# the screen(s) back to normal; can be tweaked for this purpose, though).


import subprocess
import time
import datetime as dt
import invscr  # script in the same directory

check_every = 300  # seconds. See below.
# invert_hour: when to invert the screen(s). Format: hour, minute, second.
invert_hour = dt.time(22, 15, 00)

while True:
    today = dt.date.today()  # datetime.date(y, m, d)
    now = dt.datetime.now()  # datetime.datetime(y, m, d, h, min, s, ms)
    invert_time = dt.datetime.combine(today, invert_hour)

    # seconds before block
    allowedtime = dt.timedelta.total_seconds(invert_time - now)

    if 0 < allowedtime < check_every:
        # Inversion is imminent! Sleep the precise amount of time
        # before inversion (and hope the computer won't be suspended in the
        # meanwhile. But no big deal: this would only delay the inversion by 
        # check_every in the worst case).
        time.sleep(allowedtime)
        invscr.invscr()  # flip the screen(s)

    # sleep a little (to spare CPU).
    time.sleep(check_every)
    # This is to avoid an issue with naive time.sleep(blockfrom - now),
    # which won't work if the computer has been suspended (the blocking will
    # happen too late, since the counter for time.sleep won't have been
    # incremented during the time the computer was suspended).