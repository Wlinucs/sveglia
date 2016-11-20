import time
import os
import winsound

not_executed = 1

a=int(input("ora: "))
b=int(input("minuti: "))

while(not_executed):
	dt = list(time.localtime())
	hour = dt[3]
	minute = dt[4]
	if hour == a and minute == b:
		winsound.Beep(100, 20000)	
		not_executed = 0