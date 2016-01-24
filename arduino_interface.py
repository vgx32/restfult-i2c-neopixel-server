import time
import serial
import sys
import threading


def connect(device):
    try:
        return serial.Serial(device, baudrate=9600)
    except:
        print("failed to connect to", device)

# assume data is a byte array
def writeData(con, data):
  print "tx:" + data.tostring()
  con.write(data)

def runDebugLog(con):
  debugThread = threading.Thread(target=debugPrints, args=(con,))
  debugThread.daemon = True
  debugThread.start()
  return debugThread

def debugPrints(con):
  while True:
    readData(con)

def readData(con):
  # con.timeout
  data = con.readline()
  sys.stdout.write("RX(%s):%s" %(len(data), data))
  return data



'''
expected format:
{
  mode: <string>,
  data: [values list]
}
returns: a packet of data that can be sent to arduino to
  change the display mode/colors; has following format:
    "m0xV0..0xVn\n", where m is the mode char and 0xVi is 
    a hex value of corresponding data value
'''
def dictToPixelPacket(pixelData):
  pass



device = "/dev/ttyACM0"
arduino = connect(device)
def modeToModeChar(mode):
  modes = {
      "cycle": "\x63",
      "both": "\x62",
      "all-on": "\x61"
  }
  if mode in modes:
    return modes[mode]
  else:
    return None

testData = ("\x20\x00\x00" +
            "\x00\x20\x00" +
            "\x00\x00\x20" +
            "\x20\x20\x00")



def packagePixelData(displayMode, pixelValues):
    modeChar = modeToModeChar(displayMode)
    if modeChar:
        return (modeChar + pixelValues + "\n")
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

