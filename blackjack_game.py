#Rules of BlackJack
#The dealer deals 2 cards to the player
#Then gives himself 2 cards; one face up and one facedown
#The player then is given the option to get another card or stay
#if the player hits and busts(goes over 21), the player loses
#if player gets 21 or "BlackJack", they win
#if they stay and still arent at 21
#the dealer reveals his second card
#The dealer must hit when at 16 and must stay on 17
#Aces can be 1 or 11. They will be prompted to pick
#if the dealer goes over 21 or "busts", the player wins

#Functions of Blackjack

#deal 2 random cards to player and return sum of cards (deck should be ace, 2-10, jack, queen, and king)

#dealer draws cards, and only one card is shown to the player.

#prompt the user to draw another card, or stay at the sum of cards they have currently. If they choose to hit, deal them another random card.

#dealers second card is revealed and the dealers total is displayed to the player.

#function that makes the dealer hit until they get 17 (must hit on 16).

#compare the players total with the dealers total and print the totals, and the result of the game.

import random as rd    
deck={'1':[1,11],'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'11':10,'12':10,'13':10}  #dictionary for scoring 
#print(deck['1'][1])
#print(deck['1'][0])



#this function assigns the player 2 random cards and gives them the total. It then asks the user if they would like like to hit
#or stay. Once the user stays, it will print the players final total.
def playerhand(player_hand):
    
    pcard1 = rd.choice(list(deck))
    pcard2 = rd.choice(list(deck))
    player_hand.extend([pcard1, pcard2])
    cval1 = deck.get(pcard1)
    cval2 = deck.get(pcard2)
    card_tot = cval1 + cval2
    print('Your Cards are:',pcard1, pcard2)
    print('Your Total is:', card_tot)
    print('-------------------------------------')
    hit = 'y'
    while hit == 'y':
        hit = str(input('"y" to hit or "n" to stay: '))
        if hit == 'y':
            new_card = rd.choice(list(deck))
            player_hand.append(new_card)
            cval3 = deck.get(new_card)
            card_tot = card_tot + cval3
            print('Your Cards are:',player_hand)
            print('Your Total is:', card_tot)
            print('-------------------------------------')
            if card_tot > 21:
                print('You Have Busted! You Lose!')
                break
            elif card_tot == 21:
                print('BlackJack!')
                break
        else:
            for i in player_hand:
                if i == 'A':
                    i = input('Type 11 or 1? ')
                    x = int(i)
                    card_tot = card_tot + x
            print('Your Final Total is:',card_tot)
            print('-------------------------------------')
    return card_tot

player_hand = []
card_tot = playerhand(player_hand)



def inst():                      # Instructions 
    file=open('bj-inst.txt','r') #this is the file where we wrote the rules to BlackJack
    for line in file:
        print(line.rstrip())     # the loop reads each line of the file and then prints it
        input()                  # rstrip gets rid of the extra lines at the end
    file.close()


dealer=[]
n=0
for i in range(2):                            # this is how the dealer gets the first two cards
    a=rd.randint(1,13)
    dealer.append(a)
print(dealer[n])                              # the player is shown the first card
tot=dscore()
while tot<17:                                 # if the dealer is total is under 17 they draw another card
        n+=1
        a=rd.randint(1,13)      
        dealer.append(a)
        print(dealer[n])                      # the next card in the dealers hand will be shown
        tot=dscore()                          # the total of the dealer is checked again to see if they will draw another 

print(dealer)                                 # all the dealers cards are shown
print("the dealer's final total is:", tot )
if tot>21:
    print("the dealer Busted!")
    

def dscore():                    # function dscore scores the dealers hand         
    tot=0
    for i in dealer:
        if i=='1':               # using the running total of the dealer we decide wether the dealer will make ace worth 1 or 11
            if tot<11:
                a=deck[[str(i)][1]]  # if the dealers running total is over 11 ace's will be 1 if the total is under 11 ace's will be 1 
                tot+=a
            else:
                a=deck[[str(i)][0]]
                tot+=a
        else:
            a=deck[str(i)]
            tot+=a
            
if card_tot>tot:
    print('Congradulations! you WON!')
else:
    Print('you lost.')
