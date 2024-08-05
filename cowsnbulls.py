# Added this line from git clone

from random import seed
from random import randint
from time import time

#************************************************************************************

# This function counts no.of cows and bulls based on two number list inputs - my_num, other_num

def count_cb(my_num,other_num):				
	
	cows,bulls=0,0

	for i in range(4):

		try:
		
			index = other_num.index(my_num[i])

			if(index == i):

				bulls+=1

			elif(i>=0 and i<=3):

				cows+=1

		except ValueError:
			pass 

	return (cows,bulls)

#************************************************************************************

#This function generates 4 digit random number without zeros & repetition of digits

def rand_4dn():
	
	my_num = []

	for i in range(4):

		seed()		
	
		value = randint(1,9)
	
		while (value in my_num):	
			value = randint(1,9) 
		my_num.append(value)
	
	return my_num

#************************************************************************************

def num_predictor():
			
	pass

#************************************************************************************

class colors:
	
	RED 	= '\033[31m'
	GREEN 	= '\033[32m'
	ENDC 	= '\033[m'
	BLUE	= '\033[34m'
	PURPLE	= '\033[35m'
	CYAN	= '\033[36m'


#************************************************************************************

def input_validation(other_num):
	
	if (len(other_num)!=4):
		return False
	elif ('0' in other_num):
		return False
	elif (len(other_num)!=len(set(other_num))):
		return False
	else:
		return True
	
#************************************************************************************

def main():
	
	print(colors.PURPLE + '\n Hi Naveen! Welcome to Cows & Bulls Game !!!')
	
	play = input(colors.BLUE + '\n Do you want to play Cows & Bulls now ? Enter (y/n):\t')[0]

	while(play == 'y'):

		t1 = time()
	
		print(colors.GREEN + '\n Computer has assumed a 4 digit number without zeros & repetition of digits')

		print(' Guess the number....')

		my_nl = rand_4dn()															# Generated 4 digit random number in list type

		my_ni = int("".join(map(str, my_nl)))													# Converting list->string->int

		cb = (0,0)

		i = 0

		while(cb[1]!=4):

			i+=1

			try:

				other_ni = input(colors.RED + '\n Enter Guess no. {} :\t'.format(i))

			except SyntaxError as e:
		
				other_ni = 0

			while(input_validation(str(other_ni)) == False):

				try:
					other_ni = input('\n Invalid Input. Please Enter 4 digit number without zeros & repetition of digits:\t') 

				except SyntaxError as e:

					other_ni = 0

			other_nl = [int(x) for x in str(other_ni)]

			cb = count_cb(my_nl,other_nl)

			print(colors.BLUE + '\n For {} \t Cows: {}  &  Bulls: {}'.format(other_ni,cb[0],cb[1])) 

		t2 = time()

		print(colors.GREEN + '\n Congrats !!! You won within {} moves. {} seconds taken to finish the game\n'.format(i,t2-t1))

		play = input(colors.PURPLE + ' Do you want to play again ? Type (y/n):\t')

	print(colors.ENDC + '\n Bye Bye......\n')

	return ()

if(__name__ == '__main__'):
	main()

#************************************************************************************
