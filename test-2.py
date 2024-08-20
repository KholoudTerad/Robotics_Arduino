import pyfirmata2
import time

port = "COM3"
board = pyfirmata2.Arduino(port)
ledPin= board.get_pin("d:3:o")

while True:
    cmd = input("enter on or off: ")
    if cmd == "on":
        ledPin.write(1)

    elif cmd == "off":
        ledPin.write(0)


board.exit()
