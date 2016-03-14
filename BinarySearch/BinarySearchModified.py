from math import log, ceil
high = int(input("From 1 to wich number do you want the game to be? "))
print("Maximun number of guesses needed is '" + str(ceil(log(high, 2))) + "'")
low = 1
num = (high + low) // 2
tries = 0
while low != num or high != num:
	tries += 1
	answer = str(input("Is you number higher than '" + str(num) + "' [y/n] "))
	if answer == "y":
		low = num + 1
	elif answer == "n":
		high = num
	else:
		print("That is not a valid answer.")
	num = (high + low) // 2
print("Number of guesses '" + str(tries) + "'. Your number is '" + str(num) + "'.")
