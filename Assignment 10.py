# Creating a function
def pattern(input_char, line_count, display_mode):
    # Left condition
    if display_mode == 'LEFT':
        for x in range(line_count):
            print(''*(line_count-x-1)+input_char*(2*x+1))
    # Right condition        
    elif display_mode == 'RIGHT':
        for x in range(line_count):
            print('  '*(line_count-x-1)+input_char*(2*x+1))
    # Center condition        
    elif display_mode == 'CENTER':
        for x in range(line_count):
            print(' '*(line_count-x-1)+input_char*(2*x+1))

# Getting user input for the function    
input_char = input("Enter your character? ")
line_count = input("How many lines do you need? ")
display_mode = input("How do you want to justify the display (LEFT, RIGHT, CENTER)? ")
line_count = int(line_count)

# Executing the function
result = pattern(input_char, line_count, display_mode)