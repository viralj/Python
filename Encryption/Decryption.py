"""
Custom Decryption class

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

class Decryption:
 
    def decryption(str = []):
        """
        The main decryption method that we will call from the main.py file
        to run decryption class.

        This method will ask user for length of encrypted list and
        user will need to enter one by one list values.

        This function will create its own list and it will cal 'decrypt' method.
        """
        while True:
            try:
                a = int(input("What is length of your encrypted list? "))
            except ValueError:
                print()
                print("Int numbers only!")
                continue
            else:
                break

        b = []
        for x in range(0, a):
            c = 0
            while True:
                  try:
                     c = int(input("Enter encrypted list part {}: ".format(x+1)))
                  except ValueError:
                     print()
                     print("Int numbers only!")
                     continue
                  else:
                     break
            b.append(c)
        Decryption.decrypt(b)   # Lets decrypt the list data


    def decrypt(str = []):
        """
        A decryption method to decrypt the data given by
        user and list created by system.

        There is only one thing to remember which is the key functionality
        of whole decryption method.
        """
        c = []
        for a in str:
            b = (((((a*4)/12)-5)/5)-1)  # This is the key decrypter
            c.append(chr(int(b)))
        d = ''.join(c)
        print("Your decrypted string is: ", d)
