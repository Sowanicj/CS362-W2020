# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:53:31 2020

@author: J Sowanick
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["Annie"]

#number of curses and victory cards
nV = testUtility.getVics(player_names)
nC = testUtility.getCurses(player_names)

#Get boxes
box = testUtility.getBoxes(nV)

#Get supply order
supply_order = testUtility.getSupOrder()

#Pick 10 cards from box to be in the supply.
supply = testUtility.pickTen(box)

#The supply always has these cards
testUtility.setStandardSupply(supply, nV, nC, player_names)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.constructPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)