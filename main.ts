input.onButtonPressed(Button.A, function () {
    control.reset()
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    basic.pause(2000)
    basic.showIcon(IconNames.Heart)
    control.reset()
})
let Mail = 0
radio.setGroup(1)
basic.forever(function () {
    if (tinkercademy.PIR(DigitalPin.P0)) {
        Mail += 1
        basic.showNumber(Mail)
        basic.pause(2500)
        radio.sendNumber(Mail)
    } else {
        basic.showNumber(Mail)
        basic.pause(2500)
    }
})
