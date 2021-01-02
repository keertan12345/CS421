#Importng modules
import random
import string
from random import choice

#Getting user input
quote = input("Enter a quote:")

#creating a variable for the encrypted quote
cryptoquote = ""

quote_list = list(quote.upper())
order_list = list(string.ascii_uppercase)
random_list = list(string.ascii_uppercase)
random.shuffle(random_list)

for x in quote_list:
    index = -1
    if x in order_list:
        index = order_list.index(x)
    if index != -1:        
        cryptoquote = cryptoquote + random_list[index]
    else:
        cryptoquote = cryptoquote + x
        
#Printing the output
print("Quote: \n", quote)
#print(quote)
print("Crypto Quote string: \n", cryptoquote)
#print(encrypted) 
print(" Hint -->", cryptoquote[0] , "=" , quote_list[0])