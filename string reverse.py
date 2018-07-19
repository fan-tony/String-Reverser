#String Reverser
#July 19/2018

string = input("Give me characters.")
stringRev = []

for i in string:
    stringRev.insert(0,i)

print(''.join(map(str, stringRev)))

