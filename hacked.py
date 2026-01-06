import signal
import time
import random
import sys
from colorama import init, Fore

init(autoreset=True)

def handler(signum, frame):
	pass

COLORS = [
	Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

def printcolor(text):
	colored = random.choice(COLORS)
	print(f"{colored}{text}")

while True:
	signal.signal(signal.SIGINT, handler)
	printcolor("You've been hacked! lol")
	time.sleep(0.01)
