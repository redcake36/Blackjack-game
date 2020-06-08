import random

coms = ['s','m','e','q','d']

#создание колоды карт, строка - карты от 2 до туза одной масти	
cards= ["A "," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"," J"," Q"," K"]# at all 13 kinds of cards
suits = ["C","D","H","S"]# and 4 suits

def end_words(str,p,d):
	print("Your hand({}):".format(p),end ='')
	print(*mainHand, sep = '|', end = '')
	print("  Diller`s hand({}):".format(d),end ='')
	print(*dillersHand, sep = '|')
	
	print('{:#^60}'.format('  !!!{}!!!  '.format(str)))
	print('{:#^60}'.format('  RESTARTING...  '))
	input()
	game_restart()

# выбор карт с последующим удалением из колоды | т.е. карты не могут повторяться
def random_card(n,arr):
	global cardPile

	for i in range(n):
		rSuit = random.randint(0,len(cardPile)-1)

		if len(cardPile[rSuit]) == 0:
	 		cardPile.pop(rSuit)
	 		rSuit = random.randint(0,len(cardPile)-1)

		rCard = random.randint(0,len(cardPile[rSuit])-1)
		arr.append(cardPile[rSuit][rCard] + suits[rSuit]) 
		cardPile[rSuit].pop(rCard)
	arr = arr.sort()

def game_result():
	global money
	global bet

	if len(mainHand) == 0:
		print('You have no cards!!! Press -s- to start')
	else:  

		p = 0
		d = 0
		dillerFlag = True
		
		for i in range(len(mainHand)):
			if cards.index(mainHand[i][0]+mainHand[i][1]) == 0:
				if (p+11>21):
					p+=1
				else:
					p+=11
			elif cards.index(mainHand[i][0]+mainHand[i][1])>8:
				p+=10
			elif (cards.index(mainHand[i][0]+mainHand[i][1]) != 0) and (cards.index(mainHand[i][0]+mainHand[i][1]) < 9):
				p += cards.index(mainHand[i][0]+mainHand[i][1])+1
		
		if (p>21):
			end_words('You loose',p,d)
		elif (p<=21) and (p>-1):
			while dillerFlag:
				d = 0
				for i in range(len(dillersHand)):
					if cards.index(dillersHand[i][0]+dillersHand[i][1]) == 0:
						if (d+11>21):
							d+=1
						else:
							d+=11
					elif cards.index(dillersHand[i][0]+dillersHand[i][1])>8:
						d+=10
					elif (cards.index(dillersHand[i][0]+dillersHand[i][1]) != 0) and (cards.index(dillersHand[i][0]+dillersHand[i][1]) < 9) :
						d += cards.index(dillersHand[i][0]+dillersHand[i][1])+1
				
				if (d < p) and (d < 17):
					random_card(1,dillersHand)
				elif (d == p) and (d < 17):
					random_card(1,dillersHand)
				elif d > 17:
					dillerFlag = False
				else:
					dillerFlag = False

			print(bet,'11111111111111111111')

			if d > 21:
				end_words('YOU WIN',p,d)
				money += bet*2
			elif (p==21):
				end_words('BLACKJACK',p,d)
				money += bet*2.5
			elif d > p:
				end_words('You lose',p,d)
			elif d == p:
				end_words('Equal...',p,d)
				money += bet
			else:
				end_words('YOU WIN',p,d)
				money += bet*2 

def double():
	global bet
	global money
	
	money -=bet
	bet *= 2
	give_card()
	game_result()

def game_start():
	global money
	money -= bet
	random_card(2,mainHand)
	random_card(2,dillersHand)

def give_card():
	random_card(1,mainHand)

def game_restart():
	global mainHand
	global cardPile
	global dillersHand
	global splitHand
	global startFlag
	global bet

	startFlag = 0 	
	mainHand = []
	dillersHand = []
	splitHand = []
	bet = 1
	cardPile = [cards.copy() for i in range(4)]

def quit():
	global flag 
	flag = False

def something(ind):
	result = {
		's':game_start,
		'm':give_card,
		'e':game_result,
		'd':double,
		# 'r':game_restart,
		'q':quit
	}
	func=result.get(ind,lambda :'Invalid')
	return func()

if __name__ == '__main__':
	flag = True
	startFlag = 0
	money = 20
	bet = 1

	mainHand = []
	splitHand = []
	dillersHand = []
	cardPile = [cards.copy() for i in range(4)]

	print('{:#^60}'.format('  !!!WELLCOM TO A BLACKJACK GAME!!!  '))
	while flag:
		if startFlag != 0: 
			print('\nYou  have: {} $'.format(money))
			print("Your  bet: {}$\n".format(bet))

			print("Your hand:",end ='')
			print(*mainHand, sep = '|')
			if len(splitHand)>0:
				print("Your second:",end ='')
				print(*splitHand, sep = '|')

			print("Diller`s hand:",end ='')
			print('{}| /?/ \n'.format(dillersHand[0]))

			print('s - start')
			print('m - more')
			print('d - double')
			print('e - enough')
			# print('r - restart')
			print('q - quit')
		else:
			print("\nYou  have: {}$".format(money))
			print('s - start')
			print('q - quit')

		print('Enter the comand:',end=' ')
		c = input()
		
		if c in coms:
			if (startFlag == 0) and (c == 's'): 
				something(c)
				startFlag += 1
			elif (startFlag == 1) and (c == 's'): 
				print('{:#^60}'.format('  You can`t start the game twice...  '))
			else:
				something(c)
		else:
			print('{:#^60}'.format('  Please follow the instruction...  '))
