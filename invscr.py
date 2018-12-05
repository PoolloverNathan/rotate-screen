#!/usr/bin/env python3

# Simple script that inverts the computer's screen(s).
# Or rather, it gets the screen(s) into inverted mode, i.e. executing
# the script twice won't get the screen(s) back to normal.

import subprocess

def invscr():
    # Get screens
    get = subprocess.check_output(["xrandr"]).decode("utf-8").split()
    screens = [get[i-1] for i in range(len(get)) if get[i] == "connected"]

    # Invert them
    for scr in screens:
        subprocess.call(["xrandr", "--output", scr, "--rotate", "inverted"])

if __name__ == "__main__":
    invscr()
