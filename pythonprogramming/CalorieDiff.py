# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 10:11:24 2018

@author: Han
"""



balance = 0


cheese = 106
coke = 280
apple = 81
avocado = 50
banana = 100

food = ['cheese = 106', 'coke = 280', 'apple = 81', 'avocado = 50', 'banana = 100']
      



def eat():
    return balance + foodcalorie
def go_running():
    return balance - 100
def go_weight_lifting():
    return balance - 200

print('-----------------')
gender = input('What is your gender? ')

print('Welcome to the Calorie Counter.')
print('Please Choose An Option.')

a = ['Eat','Go Running','Weight Lift', 'Sleep']
# a list variance always uses zero-index --> 0 to N-1 (range(n))
for i in range(len(a)): 
    print("Option " + str(i+1) + ": " + a[i])
print('-----------------')    


while True:
    option = int(input('Choose an Option: '))
    if option == 1:
        for i in range(len(food)):
            print("Option " + str(i+1) + ": " + food[i])
        print('-----------------')
        foodoption = input("Please enter your food selection. ")
        if foodoption == "cheese":
            foodcalorie = 106
        if foodoption == "coke":
            foodcalorie = 280
        if foodoption == "apple":
            foodcalorie = 81
        if foodoption == "avocado":
            foodcalorie = 50
        if foodoption == "banana":
            foodcalorie = 100
        balance = eat()
        print('New Calorie Count: ', balance)
    if option == 2:
        if balance >= 100:
            balance = go_running()
            print(' New Balance (after running):', balance)
        else:
            print ('Cannot exercise, calories insufficient. Please eat before exercising.')
    if option == 3:
        if balance >= 100:
            balance = go_weight_lifting()
            print(' New Balance (after weightlifting):', balance)
        else:
            print ('Cannot exercise, calories insufficient. Please eat before exercising.')
    if option == 4:
        print('Calorie Count: ', balance)
        if gender == 'male' and balance >= 2500:
            print ('Thank you for using the Calorie Counter, you have met your daily calorie goal as a male.')
        if gender == 'female' and balance >= 2000:
            print ('Thank you for using the Calorie Counter, you have met your daily calorie goal as a female.')
        else:
            print ('Thank you for using the Calorie Counter, you have NOT met your daily calorie goal.')
        break
    