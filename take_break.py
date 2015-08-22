import time
import webbrowser


total_break = 3
break_count = 0

print "This program started on", time.ctime()

while break_count < total_break:
    time.sleep(10)
    print 'Current Time is', time.ctime()
    print 'Time to take a break'
    webbrowser.open("https://www.youtube.com/watch?v=zF6sF85yV9s")
    break_count += 1

print 'This program end on', time.ctime()
