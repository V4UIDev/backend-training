import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        self.contents = []
       
        self.args = args
        
        for balls in args:
            k = 0
            while k < self.args.get(balls):
                self.contents.append(balls)
                k = k + 1
   

    def ex_draw(self, draws):
        x = 0
        
        drawList = []
        contents = []
        contents = self.contents.copy()
        
        
        if draws > len(contents):
            draws = len(contents)
        while x < draws:
            randomNumber = random.randint(0, (len(contents) - 1))
            drawList.append(contents[randomNumber])
            contents.pop(randomNumber)
            x = x + 1
        
        
        return(drawList)

    def draw(self, draws):
        x = 0
        
        drawList = []
        contents = []
        contents = self.contents
        
        
        if draws > len(contents):
            draws = len(contents)
        while x < draws:
            randomNumber = random.randint(0, (len(contents) - 1))
            drawList.append(contents[randomNumber])
            contents.pop(randomNumber)
            x = x + 1
        
        
        return(drawList)

    


      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        n = 0
        addition = 0
        expected_balls_list = []
        for balls in expected_balls:
            k = 0
            while k < expected_balls.get(balls):
                expected_balls_list.append(balls)
                k = k + 1
        drawListEx = []

        while n < num_experiments:
            drawListEx = hat.ex_draw(num_balls_drawn)
            for colour in expected_balls:
                count = drawListEx.count(colour)
                if count != expected_balls.get(colour):
                    answer = 0
                    break
                else: answer = 1
            addition = addition + answer
            n = n + 1
        probability = float(addition / num_experiments)
        return probability
            


