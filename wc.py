from sys import argv
#print(argv) i learned arguments.
filename = argv

#print(filename)
filename.pop(0)


   
def wc(filename):
    txt = open(filename)

    text= txt.read()


    words = len(text.split(" "))- 1 + len(text.split("\n"))
        
    lines = len(text.split("\n"))

    letters = len(text)
    txt.close()
    print(f"{words}, {lines}, {letters}  {filename}")
 
for i in filename: 
    wc(i)
