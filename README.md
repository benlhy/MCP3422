# MCP3422
This is a library for the MCP3422 library

# Functions
* setup
* read

Note that you can change the settings any time using the setup function. Currently the microcontroller just polls the sensor when the read function is called without waiting for the ready bit to be set. It is hardcoded to continuous mode, but it can be changed easily to one shot mode.

# Install
Drag the mcp3422.py file into your .lib folder and refer to the example code.py for use.