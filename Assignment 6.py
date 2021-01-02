# All students registered in the html class
html = [ "guy", "madeline", "parker", "chris","tom", "ursula", "ramesh", 
"lisa", "staci", "jordan", "emmett", "vinny", "brian", "zora", "oliver", 
"polly", "kingston", "olivia", "xavier", "fiona", "zack", "harmony", 
"barb", "samson", "ariel", "emma", "yasmine", "crystal", "dan", "xenia", 
"irving", "tiffany", "noah", "umesh", "yates", "victoria", "desiree", 
"quinn", "wendy", "frank", "henry", "mike", "isabella", "nora", "julie", 
"lincoln", "alex", "kim", "raven", "watson", "ganga"] 

# Two lists for each section after being divided
html_a = [] 
html_b = []

# Iterating through the html class list
for x in range(len(html)):
    if html[x] < "n":
        html_a.append(html[x])
    else:
        html_b.append(html[x])

# Sorting the lists into alphabetical order
html_a.sort()   
html_b.sort()

# Printing the lists 
print("html --> ", html)
print("html_a --> ", html_a)
print("html_b --> ", html_b)