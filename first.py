import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while (break_count < total_breaks):
    time.sleep(3)
    webbrowser.open("https://www.liuchuo.net")
    break_count = break_count + 1

