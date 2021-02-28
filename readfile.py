import os

f = open("test.txt","r")

a = f.readlines()

print(type(a))

f.close()