from machine import I2C, Pin

class AD5252:
    def __init__(self, i2c, address=0x2C):
        """
        Initialize the AD5252 device.
        :param i2c: I2C object
        :param address: I2C address of AD5252, default is 0x2C
        """
        self.i2c = i2c
        self.address = address
    def write_register(self, register, value):
        """
        Write data to the specified register.
        :param register: Register address
        :param value: Value to write (0-255)
        """
        if not 0 <= value <= 255:
            raise ValueError("Value must be between 0 and 255.")
        self.i2c.writeto_mem(self.address, register, bytearray([value]))
    def read_register(self, register):
        """
        Read data from the specified register.
        :param register: Register address
        :return: Read value (0-255)
        """
        data = self.i2c.readfrom_mem(self.address, register, 1)
        return data[0]

# Initialize I2C
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

# Scan I2C devices
devices = i2c.scan()
print("I2C devices found:", [hex(addr) for addr in devices])

# Initialize AD5252
ad5252 = AD5252(i2c)

# Write to RDAC1 register
ad5252.write_register(0x00, 128)

# Read from RDAC1 register
value = ad5252.read_register(0x00)
print("RDAC1 value:", value)
