###Alphabet Triangle – Print letters in this pattern:
###A
###A B
###A B C
###A B C D

for i in range(1,5):
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print()



