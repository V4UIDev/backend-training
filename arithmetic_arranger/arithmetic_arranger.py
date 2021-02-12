import re

def arithmetic_arranger(problems, answer = False):
    x = 0
    n = 0
    symbolList = []
    arithmeticList = []
    sumLine = ""
    dashline = ""
    firstLine = ""
    secondLine = ""
 
    for problem in problems:
        x = x + 1
      
    
    while n < x:
        arithmeticNumbers = re.findall('[0-9]+', problems[n])
        symbol = re.findall('[+\-]', problems[n])
        
        for number in arithmeticNumbers:
            
            if x > 5:
                arranged_problems = "Error: Too many problems."
                return arranged_problems
            elif symbol == []:
                arranged_problems = "Error: Operator must be '+' or '-'."
                return arranged_problems
            elif len(arithmeticNumbers) != 2:
                arranged_problems = "Error: Numbers must only contain digits."
                return arranged_problems
            elif int(number) > 9999:
                arranged_problems = "Error: Numbers cannot be more than four digits."
                return arranged_problems

        symbolList.append(symbol[0])
        arithmeticList.append(arithmeticNumbers)
        n = n + 1
    n = 0        
    for numbers in arithmeticList:
        if len(numbers[0]) > len(numbers[1]):
            dashline = dashline + ("-" * (len(numbers[0]) + 2))
            dashlength = (len(numbers[0]) + 2)
        elif len(numbers[1]) > len(numbers[0]):
            dashline = dashline + ("-" * (len(numbers[1]) + 2))
            dashlength = (len(numbers[1]) + 2)
        elif len(numbers[1]) == len(numbers[0]):
            dashline = dashline + ("-" * (len(numbers[1]) + 2))
            dashlength = (len(numbers[1]) + 2)
        
        alignNumberSec = (len(numbers[1]) + 2)
        firstLine = firstLine + '{:>{}s}'.format(numbers[0], dashlength)
        firstLine = firstLine + "    "
        secondLine = secondLine + symbolList[n] + '{:>{}s}'.format(numbers[1], (dashlength - 1))
        secondLine = secondLine + "    "
        dashline = dashline + "    "

        if symbolList[n] == "+":
            sum = (int(numbers[0]) + int(numbers[1]))
        elif symbolList[n] == "-":
            sum = (int(numbers[0]) - int(numbers[1]))

        sumLine = sumLine + '{:>{}s}'.format(str(sum), dashlength)
        sumLine = sumLine + "    "
        n = n + 1


    dashline = dashline.rstrip()
    firstLine = firstLine.rstrip()
    secondLine = secondLine.rstrip()
    sumLine = sumLine.rstrip()

    if answer == True:
        arranged_problems = firstLine + "\n" + secondLine + "\n" + dashline + "\n" + sumLine
    elif answer == False:
        arranged_problems = firstLine + "\n" + secondLine + "\n" + dashline
    



    
    return arranged_problems