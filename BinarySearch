try: # We are using try and except to make sure that the program can handle a possible errors like a StackOverflow or InvalidData.
	last = 1 + int(input("From 1 to which number do you want the game to be?\n")) #This time we did in the same line input and int functions.
	first = 1 #Initialize variables before using them so that the program doesn't get an error. 
	counter = 0 #Use this to count how many questions had to be asked
	while first!=last: #Use this conditions to make sure the game doesn't end until it has guessed the number
		x = (first+last)//2 #We calculate the average to see if we have guessed correctly by comparing it in the next line.
		if x==first or x==last:
			first = last #we do this make both of these variables equal to exit the while loop
		else:
			answer = int(input("Is your number higher or equal to " + str(x) + ". 1 for yes or 2 for no.\n")) #We ask the question to keep guessing.
			if answer == 1:
				first = x
				counter = 1+counter
			elif answer == 2:
				last = x
				counter = 1+counter
			else:
				print("Please decide between 1 or 2 only.")
	print("Your number is " + str(x) +" and had to ask " + str(counter) + " questions.") # Remember to use the string tipe casting so we don't get an error for summing two different data types.
except:
	print("Please follow the correct instructions")
input("Press enter to exit")
