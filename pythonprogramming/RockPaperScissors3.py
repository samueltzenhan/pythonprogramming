# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:04:22 2018

@author: Han
"""

user1 = input("Player 1: What is your name? ")
user2 = input("Player 2: What is your name? ")
for i in range(3): 
    user1answer = input(str(user1) + ", please choose 'rock,' 'paper,' or 'scissors.' ")
    if user1answer == 'rock' or user1answer == 'paper' or user1answer == 'scissors': 
        print('Valid Input')
        break
    if user1answer != 'rock' or user1answer != 'paper' or user1answer != 'scissors':
        print ("You need to enter in 'rock,' 'paper,' or 'scissors.'")    
 
       
   #         print ("Restart game")
       # user1answer = input(str(user1) + ", please choose 'rock,' 'paper,' or 'scissors.' ")

    
"""
for user1answer in range (3):
    if user1answer == 'rock' or 'paper' or 'scissors':
        print("Player1: Guess again with the right entry") 
        input(str(user1) + ", please choose 'rock,' 'paper,' or 'scissors' again. ")
        break
"""

#user2answer = input(str(user2) + ", please choose 'rock,' 'paper,' or 'scissors.' ")
for i in range (3):
    user2answer = input(str(user2) + ", please choose 'rock,' 'paper,' or 'scissors.' ")
    if user2answer == 'rock' or user2answer == 'paper' or user2answer == 'scissors': 
        print('Valid Input')
        break
    if user2answer != 'rock' or user2answer != 'paper' or user2answer != 'scissors':
        print ("You need to enter in 'rock,' 'paper,' or 'scissors.'")
#u1 = user1answer...
#u2 = user2answer...

     

if user1answer == 'rock':
    if user2answer == 'scissors':
        print(str(user1) + " wins, rock beats scissors.")
    elif user2answer != 'rock' + 'paper' + 'scissors':
        print("Invalid entry. Please choose 'rock,' 'paper,' or 'scissors' next time.")
    else:
        print(str(user2) + " wins, paper beats rock.")
elif user1answer == 'scissors':
    if user2answer == 'paper':
        print(str(user1) + " wins, scissors beats paper.")
    else:
        print(str(user2) + " wins, rock beats scissors.")
elif user1answer == 'paper':
    if user2answer == 'rock':
        print(str(user1) + " wins, paper beats rock.")
    else:
        print(str(user2) + " wins, scissors beats paper.")
elif user1answer == user2answer:
    print("It's a tie.")
else: 
    print("Invalid entry. Please choose 'rock,' 'paper,' or 'scissors' next time.")     
    
