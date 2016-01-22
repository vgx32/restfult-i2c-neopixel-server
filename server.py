# import smbus
import time
import serial
# bus = smbus.SMBus(1)

def connect(device):
    try:
        arduino = serial.Serial(device, 9600)
        return arduino
    except:
        print("failed to connect to", device)

# address = 0x04

# def writeNumber(value):
#     bus.write_byte(address, ord(value))
#     return -1

# def readNumber():
#     number = bus.read_byte(address)
#     return number
device = "/dev/ttyACM0"
arduino = connect(device)


while True:
    # var = raw_input("Enter 1 - 9: ")
    # if not var:
    #     continue

    arduino.write("XZ")
    # print "RPI: Hi Arduino, I sent you ", var
    time.sleep(1)

#    number = readNumber()
#    print "Arduino: Hey RPI, I received a digit ", number
#    print
