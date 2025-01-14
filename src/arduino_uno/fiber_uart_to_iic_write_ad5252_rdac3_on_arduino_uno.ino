#include <AltSoftSerial.h>
#include <Wire.h> // I2C 库

// Another solution: use SC18IM704
// https://github.com/MikroElektronika/mikrosdk_click_v2/blob/c255dddd12cc7778c01ff7df07897afccbd91989/clicks/uarttoi2c/lib_uarttoi2c/src/uarttoi2c.c
// https://www.nxp.com/products/interfaces/ic-spi-i3c-interface-devices/bridges/uart-to-ic-bridge-evaluation-board:SC18IM704-EVB

// https://www.pjrc.com/teensy/td_libs_AltSoftSerial.html
    // Board	                            Transmit Pin	  Receive Pin	    Unusable PWM
    // Teensy 3.5 / 3.6	                        21	          20	              22
    // Teensy 3.0 / 3.1 / 3.2	                  21	          20	              22
    // Teensy 2.0	                               9	          10	            (none)
    // Teensy++ 2.0	                            25	           4               	26, 27
    // Arduino Uno, Mini (& other ATMEGA328)	   9	           8	              10
    // Arduino Leonardo, Yun, Micro	             5	          13	            (none)
    // Arduino Mega	                            46	          48	              44, 45
    // Wiring-S	                                 5	           6	              4
    // Sanguino	                                13	          14	              12
AltSoftSerial altSerial;

// AD5252 的 I2C 地址（默认地址为 0x2C）
const uint8_t AD5252_ADDRESS = 0x2C;

// AD5252 寄存器地址
const uint8_t RDAC1_REGISTER = 0x01; // RDAC1 寄存器
const uint8_t RDAC3_REGISTER = 0x03; // RDAC3 寄存器

void setup() {
  // 初始化硬件串口（USB UART）
  Serial.begin(9600);
  Serial.println("AltSoftSerial and AD5252 Digital Potentiometer Test Begin");

  // 初始化 AltSoftSerial
  altSerial.begin(9600);

  // 初始化 I2C
  Wire.begin();
}

void loop() {
  uint8_t c;

  // 从硬件串口读取数据并发送到 AltSoftSerial
  if (Serial.available()) {
    c = Serial.read();
    altSerial.print(c);
  }

  // 从 AltSoftSerial 读取数据并写入 AD5252 电位器
  if (altSerial.available()) {
    c = altSerial.read(); // 读取一个字节数据
    Serial.print("Received from altSerial: 0x");
    Serial.println(c, HEX);

  // 将接收到的数据写入 AD5252 电位器
  bool success1 = writeToAD5252(RDAC1_REGISTER, c); // 写入 RDAC1 寄存器
  bool success3 = writeToAD5252(RDAC3_REGISTER, c); // 写入 RDAC3 寄存器

  // 检查写入是否成功
  if (!success1) {
    Serial.println("Error: Failed to write to RDAC1!");
  }
  if (!success3) {
    Serial.println("Error: Failed to write to RDAC3!");
  }

  }
}

// 向 AD5252 写入数据，并返回是否成功
bool writeToAD5252(uint8_t registerAddress, uint8_t value) {
  Wire.beginTransmission(AD5252_ADDRESS); // 开始 I2C 传输
  Wire.write(registerAddress); // 写入寄存器地址
  Wire.write(value); // 写入数据
  uint8_t result = Wire.endTransmission(); // 结束 I2C 传输并检查 ACK

  // 打印调试信息
  Serial.print("Value written to AD5252 (Register 0x");
  Serial.print(registerAddress, HEX);
  Serial.print("): 0x");
  if (value < 0x10) {
    Serial.print("0"); // 补零
  }
  Serial.println(value, HEX);

  // 检查 I2C 通信结果
  if (result == 0) {
    Serial.println("I2C write successful!");
    return true; // 成功
  } else {
    Serial.print("I2C write failed with error code: ");
    Serial.println(result);
    return false; // 失败
  }
}