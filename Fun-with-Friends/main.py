"""
Fun with Friends
/*
 *	Author Name: Viral Joshi
 *
 *	Join me on 	 github		: /viralj
 *				 facebook	: /viral4ever
 *				 google+	: /+ViralJoshi
 *				 twitter	: /viralhj
 *				 linkedin	: /in/viralj
 *
 *
 */
 
 required python version :    Python 3.0+
"""
import os

clear = lambda: os.system('cls')    # A lambda function to clear screen

total_question = int(input("How many funny lines you want to set up for your friends? "))
text = []

while int(total_question) > 10:
    print("Not more than 10 because it is easy to remember what you will enter.")
    print("")
    total_question = int(input("How many funny lines you want to set up for your friends? "))
