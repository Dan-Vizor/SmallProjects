#!/usr/bin/python

#size = input("size(kB): ")
size = 1000000
print("start")
doc = open("u.txt","w")
for y in range(0,size):
    for x in range(0,999):
        doc.write("        ")
        
    if y == size / 4:
        print("25%")
    if y == size / 2:
        print("50%")
    if y == size / 4 * 3:
        print("75%")
doc.close()
print("end")
