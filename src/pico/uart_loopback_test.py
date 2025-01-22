from machine import Pin, I2C, UART
import time
import random

# Initialize UART1
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))  # Adjust pins based on your hardware

# Function to generate a random string of a given length
def generate_random_string(length=10):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(chars[random.randint(0, len(chars) - 1)] for _ in range(length))

# UART loopback test function
def uart_loopback_test():
    error_count = 0
    max_attempts = 1000  # Maximum number of test attempts
    print("Starting UART loopback test...")
    for i in range(max_attempts):
        # Generate a random string
        send_string = generate_random_string()
        print(f"Sent: {send_string}")
        # Send the string
        uart1.write(send_string)
        # Wait for data to be received
        time.sleep(0.1)  # Adjust delay as needed
        # Read the echoed data
        recv_string = uart1.read(len(send_string))  # Read the same number of bytes as sent
        if recv_string:
            recv_string = recv_string.decode('utf-8')  # Convert bytes to string
            print(f"Received: {recv_string}")
            # Check if sent and received strings match
            if recv_string != send_string:
                print(f"Error: Sent '{send_string}' does not match received '{recv_string}'!")
                error_count += 1
                break  # Exit the loop on error
        else:
            print("Error: No data received!")
            error_count += 1
            break  # Exit the loop on error
    # Print test results
    if error_count == 0:
        print("Test successful! All data matched.")
    else:
        print("Test failed! Errors detected.")

# Run the test
uart_loopback_test()
