# UART on FIBER to I2C on COAX CABLE

## Prototype version 1

<details>

  <summary> click me to show images of prototype version 1</summary>

  ![3d model top](JLCEDA/images/fiber_uart_to_coax_i2c_top.png)
  ![3d model bottom](JLCEDA/images/fiber_uart_to_coax_i2c_btm.png)
  ![prototype version 1](JLCEDA/images/prototype_ver_1.png)

</details>

### bugs
- receiver inverter not needed
- pcb size not matched with case
- led logic reversed


## Prototype version XIAO

<details>

  <summary> click me to show images of prototype version XIAO</summary>

  ![3d model top](JLCEDA/images/fiber_uart_to_coax_i2c_top_xiao.png)
  <!-- ![3d model bottom](JLCEDA/images/fiber_uart_to_coax_i2c_btm_xiao.png) -->
  <!-- ![prototype version XIAO](JLCEDA/images/prototype_ver_xiao.png) -->

</details>

### features
- use XIAO RPI-2350 instead of standard rpi-pico
- LED logic fixed
- new vertical mounted LED added
- remove inverter

### bugs (placeholder)


## Usage
- connect UART TX/RX fiber cable
- connect I2C SDA/SCL coax cable
- set I2C target board VOLTAGE by 6-way switch
- power up both boards