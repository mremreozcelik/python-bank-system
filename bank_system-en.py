# -*- coding: utf-8 -*-
"""
Github Project

@author: mremreozcelik
"""

######## ENGLİSH LANGUAGE #########
        
money = int(0)
while True:
    print("Money : ", int(money)," $")
    print("1-) To deposit money (1) \n2-) Withdraw (2) \n3-) My Bank Status (3)")
    x = input("Enter the action you want to do ?\n")
    if x=="1":
        yatir = int(input("How Many Money You Want to Deposit ? (Ex: 25)\n"))
        money = int(money) + int(yatir)
        print("Congratulations " , int(yatir) , " you deposit.")
        print("Returning to the beginning...")
    elif x =="2":
        cek = int(input("How Many Money Do You Want ? (Ex: 25)\n"))
        money = int(money) - int(cek)
        print("Congratulations " , int(cek) , " you took.")
        print("Returning to the beginning...")
    elif x=="3":
        print("Instant Money :", int(+money) )        
    else:
        print("You made an incorrect entry!")