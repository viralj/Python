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

"""
We want uses to choose not more then 10 lines so we can keep this
small function.
"""
while int(total_question) > 10:
    print("Not more than 10 because it is easy to remember what you will enter.")
    print("")
    total_question = int(input("How many funny lines you want to set up for your friends? "))

"""
According to entered range by user, we will ask to enter funny lines
and we will store these lines into a dictionary.
"""
for i in range(total_question):
    v = input("Enter sentence no {} : ".format(i+1))
    while not v:
        print("Please enter something.")
        v = input("Enter sentence no {} : ".format(i+1))
    text.append(v)

"""
To clean screen.
"""
close = 0
while close is not 50:
    close = int(input("Enter 50 to clear screen and ask your "
                      "friends to choose a number between 1 and {}: ".format(total_question)))
clear()

"""
Real fun begins from here. User can ask friends to select a number
and we will show what line was there.
And then we will exit the program.
"""
a = 99
while a is not 100:
    a = int(input("Enter number between 1 and {} : ".format(total_question)))
    if a is 0:
        print("No zero please.")
    elif a is 100:
        break
    elif a > total_question:
        print("Not a valid number, please try again")
    else:
        print(text[a - 1])
        print("To exit enter 100.")

"""
Program ends here.
"""
exit()
