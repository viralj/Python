"""
Custom Encryption class

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

class Encryption:


    def encryption(str):
        """
        The main encryption method that we will call from main.py file
        to encrypt entered string by user.

        This method will create a list of entered string and will
        call the 'enc_string_list' method to encrypt the data.
        """
        a = list(str)
        enc_string = []
        for x in range(0,len(str)):
            enc_string.append(ord(a[x]))
        Encryption.enc_string_list(enc_string)

    def enc_string_list(some_list = []):
        """
        A string encryption method to encrypt given string by user.
        """
        string = []
        for a in some_list:
            b = ((((int(a)+1)*5)+5)*12)/4   # The key for custom encryption
            string.append(int(b))
        print(string, "and length of encrypted string is :", len(string))
