#   To check address: sudo i2cdetect -y 1

import smbus

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

#check your PCF8591 address by type in 'sudo i2cdetect -y -1' in terminal.
def setup(Addr):
    global address
    address = Addr

def read(chn): #channel
    try:
        bus.write_byte(address, 0x40 | chn)  # 01000000
        bus.read_byte(address) # dummy read to start conversion
    except Exception as e:
        print ("Address: %s" % address)
        print (e)
    return bus.read_byte(address)

def write(val):
    try:
        bus.write_byte_data(address, 0x40, int(val))
    except Exception as e:
        print ("Error: Device address: 0x%2X " % address)
        print (e)
