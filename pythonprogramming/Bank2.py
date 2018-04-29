# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 10:11:24 2018

@author: Han
"""

balance = 1000000000

def deposit_def(balance, deposit):
    return balance + deposit
def withdrawal_def(balance, withdrawal):
    return balance - withdrawal

print('-----------------')
print('Welcome to the Bank.')
print('Please Choose An Option.')

a = ['Withdrawal','Deposit','Check Balance', 'Exit']
# a list variance always uses zero-index --> 0 to N-1 (range(n))
for i in range(len(a)): 
    print("Option " + str(i+1) + ": " + a[i])
print('-----------------')    


while True:
    option = int(input('Choose an Option: '))
    if option == 1:
        withdrawal = int(input('How much to withdraw? '))
        if balance >= withdrawal:
            balance = withdrawal_def(balance, withdrawal)
            print(' New Balance:', balance)
        else:
            print ('Cannot withdraw, Balance insufficient. You can only withdraw up to: ',balance)
    
    if option == 2:
        deposit = int(input('How much to deposit? '))
        balance = deposit_def(balance, deposit)
        print('New Balance: ', balance)
    if option == 3:
        print('Balance: ', balance)
    if option == 4:
        print ('Thank you for using the Bank')
        break
    