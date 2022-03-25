import time
import replit
def typewriter(t):
	y=0
	while y <= len(t):
		replit.clear()
		print(t[:y])
		time.sleep(0.05)
		y = y + 1
	time.sleep(0.5)

