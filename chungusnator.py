print("On a scale of 1-10, how big do you like your chungus?")
try:
    chungus = input()
    chungusSize = int(chungus)
except:
    chungusSize = -1

def chungus_write(chungusSize):
    chungusWrite = "BIG "
    while True:
        if chungusSize > 1:
            chungusWrite = chungusWrite + "BIG "
            chungusSize = chungusSize - 1
        else:
            chungusWrite = chungusWrite + "CHUNGUS"
            return chungusWrite

if chungusSize < 0:
    print("Please insert a number between 1 and 10!")
elif chungusSize > 10:
    print("Please insert a number between 1 and 10!")
else:
    chungusPrint = chungus_write(chungusSize)
    print(chungusPrint)
end = input()


       



