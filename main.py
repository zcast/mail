def on_button_pressed_a():
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    basic.pause(2000)
    basic.show_icon(IconNames.HEART)
    control.reset()
radio.on_received_string(on_received_string)

Mail = 0
radio.set_group(1)

def on_forever():
    global Mail
    if tinkercademy.PIR(DigitalPin.P0):
        Mail += 1
        basic.show_number(Mail)
        basic.pause(2500)
        radio.send_number(Mail)
    else:
        basic.show_number(Mail)
        basic.pause(2500)
basic.forever(on_forever)
