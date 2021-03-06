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
  print("tx:" + data.tostring())
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


testJSON = {
  "mode": "cycle",
  "data": [
      0x20, 0x10, 0x53,
      0x01, 0x02, 0x15,
      0x04, 0x15, 0x06,
      0x07, 0x08, 0x07
  ]
}

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
def pack_pixel_data(pixelData):
  if "mode" in pixelData and "data" in pixelData:
    modeChar = mode_to_header(pixelData["mode"])
    data = pixelData["data"]
    if isinstance(data, list) and modeChar:
      stringedData = modeChar + ''.join(map(chr, data)) + "\n"
      return  stringedData.encode('utf-8') 
  return None

# undo the conversion from a pack_pixel_data call
def unpack_pixel_data(packedData):
  #TODO: tomorrow
  pass

# assume input is a dict object with mode and all pixel values set
def set_pixel_values(pixelData):
  packed = pack_pixel_data(pixelData)
  if packed:
    arduino.write(packed)
  else:
    print("Error: data wasn't formatted properly")

# read the current pixel values from the arduino and return them
# as a dict
def get_pixel_values():
  # TODO: requires arduino implementation
  pass


device = "/dev/ttyACM0"
arduino = connect(device)
def mode_to_header(mode):
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


def main():
    while True:
        text = raw_input("Enter text to send to Arduino ")
        if not text:
            continue

        arduino.write(text)
        print("Sent %s to arduino " % text)
        time.sleep(1)

        result = serial.read()

