# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:48:10 2018

@author: Han
"""

import random

lowerLetterCase = 'abcdefghijklmnopqrstuvwxyz'
upperLetterCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mixedLetterCase = lowerLetterCase+ upperLetterCase
mixedLetterAndNumberCase = mixedLetterCase + '0123456789'
mixedLetterAndNumberAndSpecialCase = mixedLetterAndNumberCase + '+-*@#$!%&'

difficultyLevel = input('How hard do you want your password? (low/medium/high/vault): ')
passwordLen = int(input('How long do you want to design your password?: '))

password = ''

for i in range(passwordLen):
    if (difficultyLevel == 'low'):
        password = password + lowerLetterCase[random.randint(0, len(lowerLetterCase)-1)]
    elif (difficultyLevel == 'medium'):
        password = password + mixedLetterCase[random.randint(0, len(mixedLetterCase)-1)]
    elif (difficultyLevel == 'high'):
        password = password + mixedLetterAndNumberCase[random.randint(0, len(mixedLetterAndNumberCase)-1)]
    else:
        password = password + mixedLetterAndNumberAndSpecialCase[random.randint(0, len(mixedLetterAndNumberAndSpecialCase)-1)]
        
print('Your password: ' + password)