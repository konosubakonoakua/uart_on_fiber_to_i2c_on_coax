import board
import busio
import time

# Initialize I2C
# i2c = busio.I2C(board.SCL, board.SDA)
i2c = busio.I2C(board.GP9, board.GP8)

# Initialize UART (AltSoftSerial replacement)
# uart = busio.UART(board.TX, board.RX, baudrate=9600)
uart = busio.UART(board.GP4, board.GP5, baudrate=115200) # tx--GP4 rx--GP5

# AD5252 I2C address (default is 0x2C)
AD5252_ADDRESS = 0x2C

# AD5252 register addresses
RDAC1_REGISTER = 0x01  # RDAC1 register
RDAC3_REGISTER = 0x03  # RDAC3 register

def write_to_ad5252(register_address, value):
    """
    Write data to AD5252.
    :param register_address: Register address
    :param value: Value to write (0-255)
    :return: Whether the write was successful
    """
    try:
        # Create I2C device object
        with busio.I2CDevice(i2c, AD5252_ADDRESS) as device:
            # Write register address and data
            device.write(bytes([register_address, value]))
        print(f"Value written to AD5252 (Register 0x{register_address:02X}): 0x{value:02X}")
        print("I2C write successful!")
        return True
    except OSError as e:
        print(f"I2C write failed with error: {e}")
        return False

def main():
    print("AD5252 Digital Potentiometer Test Begin")

    while True:
        # Read data from UART
        if uart.in_waiting > 0:
            data = uart.read(1)  # Read one byte
            if data:
                value = data[0]  # Extract byte value
                print(f"Received from UART: 0x{value:02X}")

                # Write received data to AD5252 potentiometer
                success1 = write_to_ad5252(RDAC1_REGISTER, value)  # Write to RDAC1 register
                success3 = write_to_ad5252(RDAC3_REGISTER, value)  # Write to RDAC3 register

                # Check if writes were successful
                if not success1:
                    print("Error: Failed to write to RDAC1!")
                if not success3:
                    print("Error: Failed to write to RDAC3!")

        # Add a small delay to avoid busy waiting
        time.sleep(0.1)

# Run the main program
if __name__ == "__main__":
    main()
