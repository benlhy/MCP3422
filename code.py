# Write your code here :-)
import board
import time
import mcp3422 as mcp

bits = 18 # 18, 16, 14, 12
channel = 1 # 1, 2
gain = 1 # 1, 2, 4, 8
 
mcp.setup(bits,channel,gain)

while True:

    data = mcp.read()
    print("{:+,.2f} uV".format(data))
    print("{:+.5f} mV".format(data/1000))
    print("{:+.7f} V".format(data/1000000))
    time.sleep(1)