#prompts the user for a day of the week
day = input()

#lists the events for Monday
if (day == "MON"): 
    print("1. Attend band rehersal")
    print("2. Submit Biology homework")
elif (day == "TUE"): 
    print("1. Attend math class")
    print("2. Attend music class")
elif (day == "WED"):
    print("1. Study for Geography test")
elif (day == "THU"):
    print("1. Attend band rehersal")
    print("2. Finish math homework")
    print("3. Finish English homework")
elif (day == "FRI"):
    print("1. Attend flute lesson")
elif (day == "SAT"):
    print("1. Attend SILC Python class")
    print("2. Attend math class")
elif (day == "SUN"):
    print("1. Meet friends")
    print("2. Get ready for school")
else:
    print("Error! Please enter valid day of week")