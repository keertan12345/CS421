#Gets two values from the user
a = input()
b = input()

#Converting the inputs into integers
value_1 = int(a)
value_2 = int(b)

#Multiplying both values together
temporary_value = value_1 * value_2 

#Dividing the sum by 2
temporary_value = temporary_value/2

#Subtracting 3 from the quotient
temporary_value = temporary_value - 3

#Using the modulus operator
temporary_value = temporary_value % 3.14

#Adding 7 to the product
temporary_value = temporary_value + 7

#Using the floor division operator
temporary_value = temporary_value//3

#Using the exponents operator
temporary_value = temporary_value ** 2

#Assignming the temporary value to the output
output = temporary_value

#printing the final product after these four operations
print("After all operations the output is", output)