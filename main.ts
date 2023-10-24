controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    myVar = 0
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    myVar += 1
})
function myFunction () {
    game.splash("" + "My var is " + ("" + myVar))
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    myFunction()
})
let myVar = 0
myVar = 0
