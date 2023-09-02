import serial
import winsound
import turtle

pen = turtle.Turtle()
leftright = True
pen.color("blue")

def move_right():
    pen.setheading(0)
    pen.forward(5)

def move_left():
    pen.setheading(180)
    pen.forward(5)

def move_up():
    pen.setheading(90)
    pen.forward(5)

def move_down():
    pen.setheading(270)
    pen.forward(5)

s = serial.Serial("COM3", 115200)
value2 = 0
print(s)

while True:
    if str(s.readline().strip()) == "b'en'":
        print("Direction switch!")
        if leftright == True:
            leftright = False
        elif leftright == False:
            leftright = True

    else: 
        value1 = int(float(s.readline().strip()))
        if value2 > value1 and leftright == True:
            print ("Left")
            winsound.Beep(1400, 100)
            move_left()
            value2 = value1
        elif value2 < value1 and leftright == True:
            print ("Right")
            winsound.Beep(1350, 50)
            move_right()
            value2 = value1
        elif value2 < value1 and leftright == False:
            print ("Down")
            winsound.Beep(1350, 50)
            move_down()
            value2 = value1
        elif value2 > value1 and leftright == False:
            print ("Up")
            winsound.Beep(1350, 50)
            move_up()
            value2 = value1



