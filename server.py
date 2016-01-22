import time
import serial

def connect(device):
    try:
        return serial.Serial(device, baudrate=9600, timeout=0)
    except:
        print("failed to connect to", device)


device = "/dev/ttyACM0"
arduino = connect(device)

modes = {
    "cycle": "\x63",
    "both": "\x62",
    "allOn": "\x61"
}

testData = ("\x20\x00\x00" +
            "\x00\x20\x00" +
            "\x00\x00\x20" +
            "\x20\x20\x00")

def packagePixelData(displayMode, pixelValues):
    if displayMode in modes:
        return (modes[displayMode] + pixelValues + "\n")
    else:
        return ""

def main():
    while True:
        text = raw_input("Enter text to send to Arduino ")
        if not text:
            continue

        arduino.write(text)
        print("Sent %s to arduino " % text)
        time.sleep(1)

        result = serial.read()

