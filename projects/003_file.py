# WRITE
with open("notes.txt","w") as f:
    f.write("hello, this is the 1st line\n")
    f.write("hello, this is the 2nd line\n")
    f.write("hello, this is the 3rd line\n")

# READ
lines = []
with open("notes.txt","r") as f: 
    for line in f:
       print(line, end="")   

