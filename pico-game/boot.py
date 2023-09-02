from machine import Pin

EncA = Pin(14, Pin.IN, Pin.PULL_UP)
EncB = Pin(13, Pin.IN, Pin.PULL_UP)

position = 0

def WaitForRisingEdgeOnA():
    global position
    while EncA.value() == 0 : pass
    if    EncB.value() == 0 : position += 0.5
    else                    : position -= 0.5
    print(position)
 
def WaitForFallingEdgeOnA():
    global position
    while EncA.value() == 1 : pass
    if    EncB.value() == 1 : position += 0.5
    else                    : position -= 0.5
    print(position)
    
if EncA.value() == 0:
    WaitForRisingEdgeOnA()
while True:
    WaitForFallingEdgeOnA()
    WaitForRisingEdgeOnA()