import os
import time

bits = 8
count = 0
decimal = 0

bits = int(input("How many bits? Default 8?\n"))

while True:
	os.system("clear")

	#PRINT

	print("Binary: ", (format(count, f'0{bits}b')))
	print("Real: ", count + (decimal * (2 ** bits)))
	print("Decimal: ", decimal)

	#CALCULATE

	count += 1
	if count == 2 ** bits:
		count = 0
		decimal += 1

	time.sleep(1)
