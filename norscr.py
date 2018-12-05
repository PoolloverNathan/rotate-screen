#!/usr/bin/env python3

# Get screen(s) back to normal

import subprocess

def norscr():
    # Get screens
    get = subprocess.check_output(["xrandr"]).decode("utf-8").split()
    screens = [get[i-1] for i in range(len(get)) if get[i] == "connected"]

    # Get them back to normal
    for scr in screens:
        subprocess.call(["xrandr", "--output", scr, "--rotate", "normal"])

if __name__ == "__main__":
    norscr()