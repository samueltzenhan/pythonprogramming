# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:04:22 2018

@author: Han
"""

user1 = input("Player 1: What is your name? ")
user2 = input("Player 2: What is your name? ")
user1answer = input(str(user1) + ", please choose 'rock,' 'paper,' or 'scissors.' ")
user2answer = input(str(user2) + ", please choose 'rock,' 'paper,' or 'scissors.' ")

#u1 = user1answer...
#u2 = user2answer...


if user1answer == user2answer:
    print("It's a tie.")
elif user1answer == 'rock':
    if user2answer == 'scissors':
        print(str(user1) + " wins, rock beats scissors.")
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
else: 
    print("Invalid entry. Please choose 'rock,' 'paper,' or 'scissors' next time.")        
        