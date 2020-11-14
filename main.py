radio.onReceivedNumber(function (receivedNumber) {
    serial.writeLine("" + (receivedNumber))
    music.playTone(988, music.beat(BeatFraction.Whole))
    basic.showNumber(radio.receivedPacket(RadioPacketProperty.SignalStrength))
})
input.onGesture(Gesture.ScreenDown, function () {
    text = ""
    basic.showIcon(IconNames.No)
})
input.onButtonPressed(Button.A, function () {
    char += -1
    basic.showString(String.fromCharCode(char))
    basic.clearScreen()
})
input.onGesture(Gesture.LogoDown, function () {
    basic.clearScreen()
    radio.sendString(text)
    text = ""
    basic.showIcon(IconNames.Yes)
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    radio.sendString(serial.readString())
    basic.showLeds(`
        # # . . .
        # # . . .
        # . . # #
        # . . # .
        . . . # #
        `)
})
input.onButtonPressed(Button.AB, function () {
    text = "" + text + String.fromCharCode(char)
    basic.showLeds(`
        # . . . #
        . . # . .
        . # . # .
        . . # . .
        # . . . #
        `)
    basic.clearScreen()
})
radio.onReceivedString(function (receivedString) {
    serial.writeLine(receivedString)
    music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    char += 1
    basic.showString(String.fromCharCode(char))
    basic.clearScreen()
})
serial.onDataReceived(serial.delimiters(Delimiters.CarriageReturn), function () {
    radio.sendString(serial.readString())
    basic.showLeds(`
        # # . . .
        # # . . .
        # . . # #
        # . . # .
        . . . # #
        `)
})
input.onGesture(Gesture.ScreenUp, function () {
    basic.showString(text)
})
let text = ""
let char = 0
serial.setRxBufferSize(128)
serial.setBaudRate(BaudRate.BaudRate115200)
serial.redirectToUSB()
radio.setTransmitPower(7)
radio.setFrequencyBand(0)
radio.setGroup(1)
char = 64
radio.sendNumber(control.deviceSerialNumber())
basic.forever(function () {
	
})
