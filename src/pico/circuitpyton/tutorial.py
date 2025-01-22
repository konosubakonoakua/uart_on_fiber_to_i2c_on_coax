################################################################################
## docs
# https://learn.adafruit.com/circuitpython-essentials
# https://docs.circuitpython.org/en/latest/docs/index.html
#  https://docs.circuitpython.org/en/latest/shared-bindings/support_matrix.html
#  https://docs.circuitpython.org/en/latest/ports/raspberrypi/README.html#port-specific-modules
#  https://docs.circuitpython.org/en/latest/shared-bindings/rp2pio/index.html
#  https://learn.adafruit.com/cooperative-multitasking-in-circuitpython-with-asyncio
################################################################################

################################################################################
## code editor
# https://code.circuitpython.org/
################################################################################

################################################################################
## modules
# >>> help('modules')
# __future__        builtins          memorymap         sys
# __main__          busdisplay        microcontroller   terminalio
# _asyncio          busio             micropython       time
# _bleio            codeop            msgpack           traceback
# _eve              collections       neopixel_write    ulab
# _pixelmap         countio           nvm               ulab.numpy
# adafruit_bus_device                 digitalio         onewireio         ulab.numpy.fft
# adafruit_bus_device.i2c_device      displayio         os                ulab.numpy.linalg
# adafruit_bus_device.spi_device      epaperdisplay     paralleldisplay   ulab.scipy
# adafruit_pixelbuf errno             paralleldisplaybus                  ulab.scipy.linalg
# aesio             floppyio          picodvi           ulab.scipy.optimize
# analogbufio       fontio            pulseio           ulab.scipy.signal
# analogio          fourwire          pwmio             ulab.scipy.special
# array             framebufferio     qrio              ulab.utils
# atexit            gc                rainbowio         usb
# audiobusio        getpass           random            usb.core
# audiocore         gifio             re                usb_cdc
# audiodelays       hashlib           rgbmatrix         usb_hid
# audiofilters      i2cdisplaybus     rotaryio          usb_host
# audiomixer        i2ctarget         rp2pio            usb_midi
# audiomp3          imagecapture      rtc               usb_video
# audiopwmio        io                sdcardio          vectorio
# binascii          jpegio            select            warnings
# bitbangio         json              sharpdisplay      watchdog
# bitmapfilter      keypad            storage           zlib
# bitmaptools       keypad_demux      struct
# bitops            locale            supervisor
# board             math              synthio
# Plus any modules on the filesystem
################################################################################


################################################################################
## reset (hard)
from microcontroller import reset
reset()

## reset (soft)
from supervisor import reload
reload()
################################################################################


################################################################################
## i2c
i2c = busio.I2C(board.GP9, board.GP8)
################################################################################


################################################################################
## uart
uart = busio.UART(board.GP4, board.GP5, baudrate=115200) # tx--GP4 rx--GP5
################################################################################

