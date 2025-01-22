import board
import busio
import time
import random

# Initialize UART
uart = busio.UART(board.GP4, board.GP5, baudrate=115200) # tx--GP4 rx--GP5


# Function to generate a random string of a given length
def generate_random_string(length=50):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,()[]{}+-=/\_~<>'
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
        uart.write(send_string.encode('utf-8'))
        # Wait for data to be received
        time.sleep(0.1)  # Adjust delay as needed
        # Read the echoed data
        recv_bytes = uart.read(len(send_string))  # Read the same number of bytes as sent
        if recv_bytes:
            recv_string = recv_bytes.decode('utf-8')  # Convert bytes to string
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


#################################################################
# Test results
# Sent: GgyA[UVZaUfCkC]8]jWBJP/sc}vM\RdiXlte9+yo)=Gw.(TCj9
# Received: GgyA[UVZaUfCkC]8]jWBJP/sc}vM\RdiXlte9+yo)=Gw.(TCj9
# Sent: 4+v2JjLgwH7RTJ(9vCxd]Y}HAgNdmRIl{5YDILjEvKgr{F<wt\
# Received: 4+v2JjLgwH7RTJ(9vCxd]Y}HAgNdmRIl{5YDILjEvKgr{F<wt\
# Sent: 7kB-yND5yqNTywj[Qcx2feh-hH.y3It\z0{t3SbEzwvO>ejiBg
# Received: 7kB-yND5yqNTywj[Qcx2feh-hH.y3It\z0{t3SbEzwvO>ejiBg
# Sent: 26vVMR5P/ftou4c9<I5oqwdODaXNRd+7DtrzZWj=t{xvO39-Ec
# Received: 26vVMR5P/ftou4c9<I5oqwdODaXNRd+7DtrzZWj=t{xvO39-Ec
# Sent: h0uj0kVc)hKXx=Jn~v]01\Xx)iRhhUIky0HN=pn=Q_~+Do84h\
# Received: h0uj0kVc)hKXx=Jn~v]01\Xx)iRhhUIky0HN=pn=Q_~+Do84h\
# Sent: hB\E1<B5d_ZUK9n7Tcp+2pRMXU{I4}fUrLri.Fr+\Fr}W86=/R
# Received: hB\E1<B5d_ZUK9n7Tcp+2pRMXU{I4}fUrLri.Fr+\Fr}W86=/R
# Sent: 5(~p,2b/ln+l<C[o~u{UK}Lg(GWC/b8r,09_AxOu}6dGRZKU~n
# Received: 5(~p,2b/ln+l<C[o~u{UK}Lg(GWC/b8r,09_AxOu}6dGRZKU~n
# Sent: ,XH3/H/wpPNnxb<Z\23A,NB}{[nyQ64RB}.<e}B16ctGgDH_F\
# Received: ,XH3/H/wpPNnxb<Z\23A,NB}{[nyQ64RB}.<e}B16ctGgDH_F\
# Test successful! All data matched.
#################################################################


