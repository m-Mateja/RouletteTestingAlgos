#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 21:01:10 2021

@author: blackbear
"""

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import collections

def choiceList(pick,run):
    
     if (pick in redArray):
         print("Run:" + str(run) + " Red "+str(pick))
        
     elif (pick in blackArray):
         print("Run:" + str(run) + " Black "+str(pick))
            
     else:
         print("Run:" + str(run) + " Green "+str(pick))
         

redArray = np.array([9,30,7,32,5,34,3,36,1,27,25,12,19,18,21,16,23,14])
blackArray = np.array([28,26,11,20,17,22,15,24,13,10,29,8,31,6,33,4,35,2])
greenArray = np.array([0,00])

totalArray = np.concatenate((redArray,blackArray,greenArray))

winsLossesTotalArray = np.array([])


def oneColourDoubleUpAlgo(winsLossesTotalArray,balance,totalArray,color,bet,closingBalanceArray,gameArray,maxBet):
    
    for i in range (1000):    
            
            run = i
            pick = random.choice(totalArray)
            choiceList(pick,run)
                
            if (color == 1 and pick in blackArray):
                balance = balance-bet
                balance = balance + (bet * 2)
                print("$" + str(balance) + "\n")
                closingBalanceArray = np.append(closingBalanceArray,balance)
                bet = 5
                gameArray = np.append(gameArray,1)
                
            elif (color == 1 and pick in redArray):
                balance = balance-bet
                print('$' + str(balance) + '\n')
                closingBalanceArray = np.append(closingBalanceArray,balance)
                bet = bet * 2
                
                if bet >= maxBet:
                    break
                    
                gameArray = np.append(gameArray,0)
                
            elif (color == 2 and pick in redArray):
                balance = balance-bet
                balance = balance + (bet * 2)
                print("$" + str(balance) + "\n")
                closingBalanceArray = np.append(closingBalanceArray,balance)
                bet = 5
                gameArray = np.append(gameArray,1)
                
            elif (color == 2 and pick in blackArray):
                balance = balance-bet
                print('$' + str(balance) + '\n')
                closingBalanceArray = np.append(closingBalanceArray,balance)
                bet = bet * 2
                
                if bet >= maxBet:
                    break
                
                gameArray = np.append(gameArray,0)
                
            elif (color == 1 or 2 and pick in greenArray):
                balance = balance-bet
                print('$' + str(balance) + '\n')
                closingBalanceArray = np.append(closingBalanceArray,balance)
                bet = bet * 2
                gameArray = np.append(gameArray,0)
                
            
            if (balance >= 2550):
                winsLossesTotalArray = np.append(winsLossesTotalArray,1)
                break
            elif (balance <=0):
                winsLossesTotalArray = np.append(winsLossesTotalArray,0)
                break
                
                
            ###############################################
            
           
    print (gameArray) 
    print (closingBalanceArray)  
    
    plt.figure()
    plt.plot(closingBalanceArray)
    plt.ylabel('balance')
    plt.xlabel('runs')
    
    print (winsLossesTotalArray)
    
def switchColourOnLossAlgo(balance,totalArray,color,bet,closingBalanceArray,gameArray,maxBet):
    
    for i in range (1000):    
            
            run = i
            pick = random.choice(totalArray)
            choiceList(pick,run)
                
            if (color == 1 and pick in blackArray):
                balance = balance-bet
                balance = balance + (bet * 2)
                print("$" + str(balance) + "\n")
                closingBalanceArray = np.append(closingBalanceArray,balance)
                bet = 5
                gameArray = np.append(gameArray,1)
                
            elif (color == 1 and pick in redArray):
                balance = balance-bet
                print('$' + str(balance) + '\n')
                closingBalanceArray = np.append(closingBalanceArray,balance)
                color == 2
                bet = bet * 2
                
                if bet >= maxBet:
                    break
                    
                gameArray = np.append(gameArray,0)
                
            elif (color == 2 and pick in redArray):
                balance = balance-bet
                balance = balance + (bet * 2)
                print("$" + str(balance) + "\n")
                closingBalanceArray = np.append(closingBalanceArray,balance)
                bet = 5
                gameArray = np.append(gameArray,1)
                
            elif (color == 2 and pick in blackArray):
                balance = balance-bet
                print('$' + str(balance) + '\n')
                closingBalanceArray = np.append(closingBalanceArray,balance)
                color == 1
                bet = bet * 2
                
                if bet >= maxBet:
                    break
                
                gameArray = np.append(gameArray,0)
                
            elif (color == 1 or 2 and pick in greenArray):
                balance = balance-bet
                print('$' + str(balance) + '\n')
                closingBalanceArray = np.append(closingBalanceArray,balance)
                bet = bet * 2
                gameArray = np.append(gameArray,0)
                
                
            ###############################################
            
           
    print (gameArray) 
    print (closingBalanceArray)  
    
    plt.figure()
    plt.plot(closingBalanceArray)
    plt.ylabel('balance')
    plt.xlabel('runs')

for i in range (10):
    
    balance = 1275
    bet = 5
    maxBet = 1000

    blackOrRed = [1,2]
    color = random.choice(blackOrRed)
    print(color)

    gameArray = np.array([])
    closingBalanceArray = np.array([])
    
    oneColourDoubleUpAlgo(winsLossesTotalArray, balance, totalArray, color, bet, closingBalanceArray, gameArray, maxBet)
    #switchColourOnLossAlgo(balance, totalArray, color, bet, closingBalanceArray, gameArray, maxBet)
   
        
            
        