import camera
import socket
import machine
import time
import buzzer
try:
    import uasyncio as asyncio
except:
    upip.install('micropython-uasyncio')
    upip.install('micropython-pkg_resources')
    import uasyncio as asyncio
    
def cam():
    camera.init(0, d0 = 4, d1 = 5, d2 = 18, d3 = 19, d4 = 36
                , d5 = 39, d6 = 34, d7 = 35
                , format=camera.JPEG, framesize=camera.FRAME_VGA
                , xclk_freq=camera.XCLK_20MHz
                , xclk = 21, pclk = 22, vsync = 25, href = 23
                , siod = 26, sioc = 27, pwdn=-1, reset=-1)
    camera.quality(10)
    # wait for sensor to start and focus before capturing image
    buf = camera.capture()
    f = open('image.jpg','w')
    f.write(buf)
    f.close()
    camera.deinit()
    
    if len(buf) > 0:
        return buf
    else:    
        return "Error"

def ConstructWebPage():
    html= """"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create Internet socket interface for TCP web-server
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.1.178', 80)) # Assign and bind port 80 for HTTP web-server socket !!!Change the IP address to bind to the IP addr of ESP32
s.listen(7) # Configure for listening maximum 5 web-clients
print("Server Started! and Running at 192.168.1.178 ")

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept() # accept new connection!!!Conn is a new socket object to communicate data on new conn. addr is the clients addr
        starts = time.ticks_ms()
        conn.settimeout(3.0)
        print('Got a connection from %s' % str(addr)) # Print the client address
        request = str(conn.recv(1024)) # Collect client request
        conn.settimeout(None)
        cam = request.find("/camera")
        if cam == 6:
            buzzer.notify1()
            start = time.ticks_ms()
            camera.init(0, d0 = 4, d1 = 5, d2 = 18, d3 = 19, d4 = 36
                        , d5 = 39, d6 = 34, d7 = 35
                        , format=camera.JPEG, framesize=camera.FRAME_VGA
                        , xclk = 21, pclk = 22, vsync = 25, href = 23
                        , siod = 26, sioc = 27, pwdn=-1, reset=-1)
            camera.quality(10)
            camera.mirror(1)
            # wait for sensor to start and focus before capturing image
            buf = camera.capture()
            camera.deinit()
            camcap = time.ticks_ms()
        
            #f = open('image.jpg','w')
            #f.write(buf)
            #f.close()
            #endw = time.ticks_ms()
        
            #file = open('image.jpg','rb')
            #response = file.read()
            #file.close()
            response = buf
            end = time.ticks_ms()
        

            print(time.ticks_diff(camcap,start))
            print(time.ticks_diff(end,camcap))
            #print(time.ticks_diff(end,camcap))
            print(time.ticks_diff(end,start))
        
            conn.send('HTTP/1.1 200 OK\n') # Send the web-server response to web-client
            conn.send('Content-Type: image/jpeg\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            ends = time.ticks_ms()
        
            print(time.ticks_diff(ends,starts))
            buzzer.notify2()
            # Clsoe connection
            conn.close()
            print("Response sent")        
    except OSError as e:
        buzzer.notify3()
        print("! "+ str(e))
        conn.close()
        print('Connection closed')
    except TypeError as err:
        buzzer.notify3()
        print("!"+str(err))

