string = ''
for i in range (10):
    for j in range (i):
        string += str(i)
        
    print(string)
    string = ''