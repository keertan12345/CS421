file = open("/Users/keertan/Library/Mobile Documents/com~apple~CloudDocs/SILC python/Source_files/quotes.txt")

lines = sorted(file.readlines())

quotes = open("/Users/keertan/Library/Mobile Documents/com~apple~CloudDocs/SILC python/CS421/Assignment 16/quotes_1.txt", "a")

for x in lines:
    quotes.write(x)

file.close()
quotes.close()