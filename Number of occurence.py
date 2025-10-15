###Write a program to print No of occurence of a given string with repetition.
#Text: I am New to this office but not New to Role.
text = "I am New to this office but not New to Role"
N = text.lower().split()
for i in set(N):
    print(i,"=",N.count(i))




"""text = "ashifashif"
n = list(text)

for i in set (n):
    print(i,"=",n.count(i))"""
[
