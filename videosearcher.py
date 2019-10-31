import os, sys, subprocess
import sys

print("Enter video title: ")
filename = input()

# OPEN FILE
def open_file(filename):
    # If operating system is Windows
    if sys.platform == "win32": 
        os.startfile(filename)
    # If operating system is MACOS or LINUX
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

open_file(filename)
