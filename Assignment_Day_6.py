#%%


# Assignment Day 6

# Question 1
# For this challenge,create a bank account class that has two attributes
#*ownerName
#*Balance
#And two methods
#*deposit
#*withdraw
#As an added requirement,withdrawals may not exceed the available balance.
#Instantiate your class,make several deposits and withdrawals,and test to make sure the account
#cant be overdrawn


class bank:
    def __init__(self,ownername,balance):
        self.ownername = ownername
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount
        print("your updated balance is :", self.balance)
        
    def withdraw(self,amount):
        if(self.balance>amount):
            self.balance-=amount
            print("your updated balance is :", self.balance)
        else:
            print("you don't have enough cradit in your account, see you have only",self.balance)
            

tanu = bank("Tanu",55000)

tanu.deposit(25000)

tanu.withdraw(45000)


#%%

# Question 2
#For this challenge,create a cone class that has two attributes:
#*R=Radius
#*h=Height
#And two methods:
#*Volume = Π * r2 = (h/3)
#*Surface area : base : Π * r2 , side : Π * r * √(r2 + h2)
#Make only one class with functions,as in where required import Math.

import math
class cone:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
        
    def volume(self):
        vol = math.pi * (self.radius**2) * (self.height/3)
        print("Volume of this cone is : ",vol)
        
    def surfaceArea(self):
        area = math.pi* self.radius *(self.radius+(math.sqrt((self.radius**2)+(self.height**2))))
        print("Surface area of this cone is ",area) 
        

con = cone(4,6)

con.volume()

con.surfaceArea()

#%%     