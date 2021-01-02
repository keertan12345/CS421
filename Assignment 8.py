# Getting user input
word = input("Enter a word please: ").lower()

# Making the function
def  isPalindrome(word):
    reversed_word = word[::-1]
    
    if word == reversed_word:
        return "TRUE"
    elif word != reversed_word:
        return "FALSE"

# Printing the result(TRUE or FALSE)
result = isPalindrome(word) 
print(result)