# import spidev
# import time
# spi = spidev.SpiDev()

# spi.open(0,0)
# def analog_read(channel):
#     r = spi.xfer2([1, (8 + channel) << 4, 0])
#     adc_out = ((r[1] & 3) << 8) + r[2]
#     return adc_out
# while 1:
#     reading = analog_read(0)
#     voltage = reading * 3.3 / 1024
#     print("Reading = %d\tVoltage=%.2f" % (reading, voltage))
#     time.sleep(1)
import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)

def analog_read(channel):
    r = spi.xfer2([0x06, (0x08 + channel) << 4, 0x00])
    adc_out = ((r[1] & 0x0F) << 8) + r[2]
    return adc_out

while True:
    reading = analog_read(0)
    voltage = reading * 3.3 / 4095
    print("Reading = %d\tVoltage = %.2f" % (reading, voltage))
    time.sleep(1)