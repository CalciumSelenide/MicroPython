# Micro:Bit Technical Specifications

The Micro:Bit has **25** external connections on the edge connector of the board, which are referred to as 'pins'. The edge connector is the gold area on the right side of board as shown the figure below.

There are **5 large pins** that are also connected to holes in the board labelled: **0**, **1**, **2**, **3V**, and **GND**. And along the same edge, there are **20 small pins** that you can use when plugging the Micro:Bit into an edge connector.

<img align="left" width="250" src="../../imgs/microbit/microbitv2ege.png"/>

## Large pins

You can easily attach crocodile clips or 4mm banana plugs to the **5** large pins.

The first three, labelled **0**, **1** and **2** are flexible and can be used for many different things - which means they are often called "general purpose input and output" (shortened to GPIO). These three pins also have the ability to read analog voltages using something called an analog-to-digital converter (ADC). They all have the same function:

  * **0**: GPIO (general purpose digital input and output) with analog-to-digital convertor (ADC).
  * **1**: GPIO with ADC
  * **2**: GPIO with ADC

With the micro:bit V2, pins **0**, **1**, **2**, and the **LOGO** can also be set to work as [capacitive touch](/reference/pins/touch-set-mode) buttons.

### WARNING:

**Be careful with the power pins!**
The pins labelled **3V** and **GND** relate to the power supply of the board, and they should NEVER be connected together.


For details on the power, current and voltage limitations of the board, see [Power Supply](https://tech.microbit.org/hardware/powersupply/).

---

* **3V**: 3 volt *power output* or *power input*:
>* *Power output*: If the Micro:Bit is powered by USB or a battery, then you can use the **3V** pin as a power output to power peripherals with.
>* *Power input*: If the Micro:Bit is NOT being powered by USB or battery, you can use the **3V** pin to supply power input to the Micro:Bit.
* **GND**: attaches to ground in order to complete a circuit (required when using the **3V** pin)

---

If you hold the **GND** pin with one hand, you can program the Micro:Bit to detect yourself touching the **0**, **1** or **2** pins with your other hand, giving you three more buttons to experiment with (you just used your body to complete an electrical circuit to make "resistive touch" buttons).

## Small pins

The **20** small pins are numbered sequentially from **3-22** (these pins are not labeled on the Micro:Bit, however, they are labelled in the picture above).

Unlike the three large pins that are dedicated to being used for external connections, some of the small pins are shared with other components on the Micro:Bit board. For example, pin **3** is shared with some of the LEDs on the screen of the Micro:Bit, so if you are using the screen to scroll messages, you can’t use this pin as well.

### Micro:Bit V2 Pin Map

| Pin  | Description |
| - | - |
| **3** | GPIO shared with LED Col 3 of the LED screen; can be used for ADC and digital I/O when the LED screen is turned off. |
| **4** | GPIO shared with LED Col 1 of the LED screen; can be used for ADC and digital I/O when the LED screen is turned off. |
| **5** | GPIO shared with Button A. This lets you trigger or detect a button "A" click externally. This pin has a pull-up resistor, which means that by default it is at voltage of 3V. To replace button A on the Micro:Bit with an external button, connect one end of the external button to pin 5 and the other end to GND. When the button is pressed, the voltage on pin 5 is pulled down to 0, which generates a button click event. |
| **6** | GPIO shared with LED Col 2 of the LED screen; can be used for digital I/O when the LED screen is turned off. |
| **7** | GPIO shared with LED Col 4 of the LED screen; can be used for digital I/O when the LED screen is turned off. |
| **8, 9** | Dedicated GPIO, for sending and sensing digital signals; can also be configured for NFC. |
| **10** | GPIO shared with LED Col 5 of the LED screen;  can be used for ADC and digital I/O when the LED screen is turned off.|
| **11** | GPIO shared with Button B. This lets you trigger or detect a button "B" click externally. |
| **12** | This GPIO pin has been reserved to provide support for accessibility. |
| **13** | GPIO that is conventionally used for the serial clock (SCK) signal of the 3-wire Serial Peripheral Interface (SPI) bus. |
| **14** | GPIO that is conventionally used for the Master In Slave Out (MISO) signal of the SPI bus. |
| **15** | GPIO that is conventionally used for the Master Out Slave In (MOSI) signal of the SPI bus. |
| **16** | Dedicated GPIO (conventionally also used for SPI 'Chip Select' function). |
| **17, 18** | These pins are wired to the 3V supply, like the large '3V' pad. |
| **19, 20** | Implement the clock signal (SCL) and data line (SDA) of the I2C bus communication protocol. With I2C, several devices can be connected on the same bus and send/read messages to and from the CPU. Internally, the accelerometer and the compass are connected to i2c. |
| **21, 22** | These pins are wired to the GND pin and serve no other function. |

## Connecting to the small pins

It is recommended that an edge connector designed for the Micro:Bit be used for connections to the small pins. For available edge connectors, put "edge eonnectors for the micro:bit" into your internet search engine to find an accessory supplier.
