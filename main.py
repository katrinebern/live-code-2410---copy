def on_b_pressed():
    global myVar
    myVar = 0
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global myVar
    myVar += 1
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def myFunction():
    game.splash("" + "My var is " + str(myVar))

def on_down_pressed():
    myFunction()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

myVar = 0
myVar = 0
