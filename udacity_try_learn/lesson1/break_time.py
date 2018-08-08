import time
import webbrowser

print("This program started on " + time.ctime())

total_breaks = 3
break_count = 0
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.baidu.com")
    break_count += 1
