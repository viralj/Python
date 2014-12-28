"""
Encryption
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

from Encryption import Encryption   # Importing custom Encryption class
from Decryption import Decryption   # Importing custom Decryption class
import time     # Importing for time delay

a = str(input("Please enter ENCRYPTION or DECRYPTION : ")).lower()  # Need user input to know next action

"""
Action for Encryption or Decryption
starts from here.
"""
if a == "encryption":
    b = str(input("Please enter a string : "))
    Encryption.encryption(b)
elif a == "decryption":
    Decryption.decryption()
else:
    print("Wrong answer! Good bye...")
    time.sleep(1)
    exit()
