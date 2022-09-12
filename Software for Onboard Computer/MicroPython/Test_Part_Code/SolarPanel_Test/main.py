from machine import Pin, ADC
import time
import buzzer

print('main.py')

solarv = ADC(Pin(32,Pin.IN))
batt = ADC(Pin(33, Pin.IN))

solarv.atten(ADC.ATTN_11DB) #full range 3.3V attneuation
batt.atten(ADC.ATTN_11DB) #full range 3.3V

solarv.width(ADC.WIDTH_12BIT) #  range 0-4095 Resolution
batt.width(ADC.WIDTH_12BIT) # range 0-4095


def solarcalV(vout):
    vin = (vout * ((21600+8170)/8170))
    return vin

def solarcalI(vin):
    cur = vin/(21600+8100)
    return cur

def solar():
    x = solarv.read() + 115
    print(x)
    vout = x/4095 * 3.3
    vin = solarcalV(vout)
    cur = solarcalI(vin) * 1000
    power = cur*vin
    print('Reading from the solar panels')
    print('Voltage out: %3.3f V' %vout)
    print('Voltage in: %3.3f V' %vin)
    print('Current: %3.3f mA' %cur)
    print('Power: %3.3f mW\n' %power)

def battery():
    a = batt.read() 
    print("Raw Reading from battery: %3.3f" %a )
    a1 = a/4095 * 3.37 
    print("Reading converted to Voltage : %3.2f" %a1)
    a2 = (a1*2)/4.794 *100
    print("Percentage of the volatge from the battery total volatge %3.1f" %a2 )

def toggle(max):
    lap = 0
    while (lap < max):
        solar()
        battery()
        time.sleep(1)
        lap+=1

toggle(5)