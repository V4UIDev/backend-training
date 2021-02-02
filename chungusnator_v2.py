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

if chungusSize < 1:
    print("Please insert a number between 1 and 10!")
elif chungusSize > 10:
    print("Please insert a number between 1 and 10!")
else:
    print("Do you want the long answer? Y/N")
    answer = input()
    if answer == "Y":
        chungusList = chungus_write(chungusSize).split()
        for i in chungusList:
            print(i)
    elif answer == "N":
        print(chungus_write(chungusSize))
    else:
        print("Invalid input.")

print(" ")
print("Press enter to quit.")
end = input()


       



