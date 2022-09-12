import network

def connect():
    '''Connects the ESP32 to the Wifi. '''
                                                # Connection when there is eduroam need to be done.
    station = network.WLAN(network.STA_IF)
    ssid = 'Stockholms_stadsbibliotek'
    password = 'stockholm'
    if station.isconnected() == True:
        print("Already connected")
        print(station.ifconfig())
        return 
    station.active(True)
    station.connect(ssid, password) 
    print("Connection successful")
    print(station.ifconfig())
    
connect()
