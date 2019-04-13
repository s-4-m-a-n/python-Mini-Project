import random
import os
import time


def Word_generate(dash_word):
	all_word=[("apple","fruit"),("ball","game"),("cat","animal"),("dog","animal"),("laptop","machine")]
	random_number=(random.randint(0,100))%len(all_word)
	guess_word=all_word[random_number][0]
	guess_hint=all_word[random_number][1]

	for i in range(len(guess_word)):
		dash_word.append(' _ ')

	return guess_word,len(guess_word),guess_hint

def Display(chance,letter_try,):
	os.system('cls')
	print("\t\t\t-------------------------------|========================|--------------------------")
	print("\t\t\t ------------------------------|WELCOME TO HANG MAN GAME|-------------------------")
	print("\t\t\t-------------------------------|========================|--------------------------")
	print("\n\n\t\t\t\t\t\t\t\t No of chance Left :  ",end=" ")
	print(*chance,sep=' ')
	print("\n\n\t\t\t\t\t\t\t\t letter_try :  {}\n\n\n".format(letter_try))
	

def Guess_Display(dash_word,hint):
	#os.system('cls')
	print("\n\n\t\t\t\t\t\t",end='')
	print(*dash_word,sep='')
	print("\n")
	print( f"\t\t\t\t\t\t hint = {hint} ")
	print("\n")

	



def get_guess():
	while(True): 
		guess=input('\n\n\t\t\t\t enter guess letter :  ')
		if len(guess)>1:
			print("\n\t\t\t\t\t\tenter only one letter")
			input()
		else:
			return guess 


def function(word,length,chance,letter_try,dash_word,guess):
	if guess in letter_try:
		input(" \n\n\t\t\t\t\t\t!! you have already entered that letter !! press any key !!")

		return 
	else:	
		letter_try.append(guess)

		if guess in word:
			for i in range(length):
				if guess == word[i]:
					dash_word[i]=" "+guess+" "

					if ' _ ' not in dash_word:
						return 1

		else : 
			chance.pop()
			return 0 



		

	 
	



def main():
	chance=[' $ ',' $ ',' $ ']
	letter_try=[]
	dash_word=[]

	word,length,hint=Word_generate(dash_word)
	 
	while(len(chance)>0):
		
		
		Display(chance,letter_try)
		Guess_Display(dash_word,hint)
		guess=get_guess()
 	
		flag=function(word,length,chance,letter_try,dash_word,guess)
		if flag==1:

			break;
	
	if flag==1:
		Display(chance,letter_try)
		Guess_Display(dash_word,hint)
		input("\n\n\t\t\t\t\tcongratulation you have won ")
		
	else:
		Display(chance,letter_try)
		Guess_Display(dash_word,hint)
		print("\t\t\t\t\t\tCORRECT WORD :  {}".format(word))
		input("\n\n\t\t\t\t\t!!!! ooops game over | No chance left !!!!!! ")
		


if __name__=="__main__":

	main()
