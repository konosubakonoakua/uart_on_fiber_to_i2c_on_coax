import board
import busio
from adafruit_bus_device.i2c_device import I2CDevice

class AD5252:
    def __init__(self, i2c, address=0x2C):
        """
        Initialize the AD5252 device.
        :param i2c: I2C object
        :param address: I2C address of AD5252, default is 0x2C
        """
        self.i2c_device = I2CDevice(i2c, address)
    def write_register(self, register, value):
        """
        Write data to the specified register.
        :param register: Register address
        :param value: Value to write (0-255)
        """
        if not 0 <= value <= 255:
            raise ValueError("Value must be between 0 and 255.")
        with self.i2c_device as i2c:
            i2c.write(bytes([register, value]))
    def read_register(self, register):
        """
        Read data from the specified register.
        :param register: Register address
        :return: Read value (0-255)
        """
        with self.i2c_device as i2c:
            result = bytearray(1)
            i2c.write_then_readinto(bytes([register]), result)
            return result[0]

# Initialize I2C
i2c = busio.I2C(board.GP9, board.GP8)

# Scan I2C devices
while not i2c.try_lock():
    pass

try:
    devices = i2c.scan()
    print("I2C devices found:", [hex(addr) for addr in devices])
except Exception as e:
    raise e
finally:
    i2c.unlock()

# Initialize AD5252
ad5252 = AD5252(i2c)

# Write to RDAC1 register
ad5252.write_register(0x00, 128)

# Read from RDAC1 register
value = ad5252.read_register(0x00)
print("RDAC1 value:", value)
