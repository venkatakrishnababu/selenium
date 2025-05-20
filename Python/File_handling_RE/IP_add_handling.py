# content = file.read()  # Reads entire file
# line = file.readline()  # Reads a single line
# lines = file.readlines()  # Reads all lines into a list
#-----------------------
# file = open("example.txt", "w")
# file.write("Hello, world!")  # Overwrites file with new content
# file.writelines(["Line 1\n", "Line 2\n"])  # Writes multiple lines


## import valid ip into 1 file and invalid into another file

import re
with open("source.txt","r") as E,open('target.txt',"w+") as F:
    with open('target1.txt',"w+") as G:
        e=E.readlines()
        p ="(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])[.]){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
        for i in e:
            b=i.strip()
            if re.fullmatch(p,b):
                F.write(b+"\n")
            else:
                G.writelines(b+"\n")


