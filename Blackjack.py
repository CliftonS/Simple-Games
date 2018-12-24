'''
Created on Dec 18, 2018

@author: Clifton
'''
from array import array
import random
from random import betavariate
class Blackjack:
    Arr = [[True,True,True,True,True,True,True,True,True,True,True,True,True],[True,True,True,True,True,True,True,True,True,True,True,True,True],[True,True,True,True,True,True,True,True,True,True,True,True,True],[True,True,True,True,True,True,True,True,True,True,True,True,True]]
    
    def __init__(self, money):
        self.player = []
        self.playerT = []
        self.dealer = []
        self.dealerT = []
        self.cash = money
    
    def gamble(self, bet):
        if self.whoWin():
            self.cash += bet
        else:
            self.cash -= bet
    
    def findCash(self):
        return self.cash
    
    def deal(self):
        a = False
        while a == False:
            x = random.randint(0,12)
            y = random.randint(0,3)
            a = self.Arr[y][x]
        self.Arr[y][x] = False;
        self.player.append(x+2)
        self.playerT.append(y)
    
    def draw(self):
        a = False
        while a == False:
            x = random.randint(0,12)
            y = random.randint(0,3)
            a = self.Arr[y][x]
        self.Arr[y][x] = False;
        self.dealer.append(x+2)
        self.dealerT.append(y)
    
    def reshuffle(self):
        for i in range(4):
            for g in range(13):
                array[i][g] = True
        for i in range(len(self.player)):
            array[self.playerT[i]][self.player[i]] = False
        for i in range(len(self.dealer)):
            array[self.dealerT[i]][self.dealer[i]] = False
    
    def playerTotal(self):
        playNum =  0
        for i in range(len(self.player)):
            if(self.player[i] <= 10):
                playNum += int(self.player[i])
            else:
                playNum += 10
        return playNum
    
    def dealerTotal(self):
        dealNum = 0
        for i in range(len(self.dealer)):
            if(self.dealer[i] <= 10):
                dealNum += int(self.dealer[i])
            else:
                dealNum += 10
        return dealNum
    
    def whoWin(self):
        playNum =  self.playerTotal()
        dealNum = self.dealerTotal()
        if playNum > dealNum & playNum < 22:
            return True
        else:
            return False
        
    def reset(self):
        self.player = []
        self.playerT = []
        self.dealer = []
        self.dealerT = []
    
    def cardPrintAllPlayer(self):
        suit = "Player has: "
        for i in range(len(self.player)):
            num1 = self.player[i]
            num2 = self.playerT[i]
            if(num1 > 10):
                if(num1 == 11):
                    suit += "Jack"
                elif(num1 == 12):
                    suit += "Queen"
                elif(num1 == 13):
                    suit += "King"
                elif(num1 == 14):
                    suit += "Ace"
            else:
                suit += str(num1)
            suit += " of "
            if(num2 == 0):
                suit += "Spades, "
            elif(num2 == 1):
                suit += "Clubs, "
            elif(num2 == 2):
                suit += "Diamonds, "
            else:
                suit += "Hearts, "
        return suit
    
    def printFirstCardDealer(self):
        suit = "Dealer has: "
        num1 = self.dealer[0]
        num2 = self.dealerT[0]
        if(num1 > 10):
            if(num1 == 11):
                    suit += "Jack"
            elif(num1 == 12):
                    suit += "Queen"
            elif(num1 == 13):
                    suit += "King"
            elif(num1 == 14):
                    suit += "Ace"
        else:
            suit += str(num1)
        suit += " of "
        if(num2 == 0):
            suit += "Spades, "
        elif(num2 == 1):
            suit += "Clubs, "
        elif(num2 == 2):
            suit += "Diamonds, "
        else:
            suit += "Hearts, "
        return suit
    
    def cardPrintAllDealer(self):
        suit = "Dealer has: "
        for i in range(len(self.dealer)):
            num1 = self.dealer[i]
            num2 = self.dealerT[i]
            if(num1 > 10):
                if(num1 == 11):
                    suit += "Jack"
                elif(num1 == 12):
                    suit += "Queen"
                elif(num1 == 13):
                    suit += "King"
                elif(num1 == 14):
                    suit += "Ace"
            else:
                suit += str(num1)
            suit += " of "
            if(num2 == 0):
                suit += "Spades, "
            elif(num2 == 1):
                suit += "Clubs, "
            elif(num2 == 2):
                suit += "Diamonds, "
            else:
                suit += "Hearts, "
        return suit
    
game = Blackjack(10)

stay = 0
hit = 1
bet = 0
gamble = 0
while stay != 1:
    #Simplified gambling
    print("How much do you want to bet? You have " + str(game.findCash()))
    bet = int(input())
    while bet > game.findCash() | bet < 0:
        print("You dont have that much money. Re-enter a valid amount")
        bet = int(input())    
    game.reset()
    hit = 0;
    game.deal()
    game.deal()
    print(game.cardPrintAllPlayer())
    game.draw()
    game.draw()
    print(game.printFirstCardDealer())
    while hit != 1:
        print("Do you want to hit or stand? Stand is 1 and hit is any other integer")
        hit = int(input())
        if hit != 1:
            game.deal()
            if(game.playerTotal() > 21):
                print("Your total is over 21, you lose")
                hit = 0
        print(game.cardPrintAllPlayer() + "\nTotal is: " + str(game.playerTotal()))
    while game.dealerTotal() < 17:
        game.draw()
    if game.dealerTotal() > 21:
        print(game.cardPrintAllDealer() + "\nYou win, the dealer overdrew!")
    else:
        if game.whoWin():
            print(game.cardPrintAllDealer() + "\nDealer: " + str(game.dealerTotal()))
            print("You have more total than the dealer, you win!")
        else:
            print(game.cardPrintAllPlayer() + "\nPlayer: " + str(game.playerTotal()))
            print(game.cardPrintAllDealer() + "\nDealer: " + str(game.dealerTotal()))
            print("You have less or equal to the dealer, you lose!")
    game.gamble(bet)
    print("You now have " + str(game.findCash()))
    print("Do you want to continue playing? Type 1 to stop, or any other integer to continue")
    stay = int(input())