import digitalio
import board
import time
import adafruit_ssd1306
import adafruit_bme680
import adafruit_ltr329_ltr303
import busio
import gfx  # graphics and shape rendering module
from digitalio import DigitalInOut

i2c = busio.I2C(scl = board.PA13, sda = board.PA12)
light_sensor = adafruit_ltr329_ltr303.LTR329(i2c)

spi = busio.SPI(board.PA17, MOSI=board.PB23, MISO=board.PB22)  # init the SPI bus
dc_pin = DigitalInOut(board.PA19)  # board pin D9
reset_pin = DigitalInOut(board.PA16)  # board pin D5
cs_pin = DigitalInOut(board.PA18)  # board pin D6
oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, dc_pin, reset_pin, cs_pin)  # 128 x 64 pixel SSD1306 display

graphics = gfx.GFX(128, 64, oled.pixel)  # initiate gfx class

AQI_cs_pin = DigitalInOut(board.PA22)  # board pin D12
AQI_sensor = adafruit_bme680.Adafruit_BME680_SPI(spi, AQI_cs_pin)
AQI_sensor.sea_level_pressure = 1013.25  # set the sea level pressure

pin_D10 = digitalio.DigitalInOut(board.PA20)
pin_D10.direction = digitalio.Direction.OUTPUT

pin_NEO = digitalio.DigitalInOut(board.PB03)
pin_NEO.direction = digitalio.Direction.OUTPUT

while True:
    
    # access the pressure readings
    temperature = AQI_sensor.temperature
    gas = AQI_sensor.gas
    relative_humidity = AQI_sensor.relative_humidity
    pressure = AQI_sensor.pressure
    altitude = AQI_sensor.altitude
    IR = light_sensor.ir_light
    vis_plus_IR = light_sensor.visible_plus_ir_light
    vis = vis_plus_IR - IR
    
    oled.fill(0)
    oled.text(f"Temp: {temperature:.1f} C", 0, 0, 1)
    oled.text(f"Gas: {gas} ohms", 0, 10, 1)
    oled.text(f"Humidity: {relative_humidity:.1f} %", 0, 20, 1)
    oled.text(f"Pressure: {pressure:.1f} hPa", 0, 30, 1)
    oled.text(f"Altitude: {altitude:.1f} m", 0, 40, 1)
    oled.text(f"Visible Light: {vis:.1f} lux", 0, 50, 1)
    oled.text(f"IR Light: {IR:.1f} lux", 0, 60, 1)
    oled.show()
    
    pin_D10.value = True
    pin_NEO.value = True

    time.sleep(0.1)
    
    pin_D10.value = False
    pin_NEO.value = False

    time.sleep(0.1)

# print(pin_D10.value)
# print("Done printing")
