import camera
import upip
import machine
import time

try:
    import picoweb
except:
    upip.install('picoweb')
    import picoweb
try:
    import uasyncio as asyncio
except:
    upip.install('micropython-uasyncio')
    upip.install('micropython-pkg_resources')
    import uasyncio as asyncio


app = picoweb.WebApp('app')

try:
    import ulogging as logging
except:
    upip.install('micropython-ulogging')
    import ulogging as logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('app')

led = machine.Pin(2, machine.Pin.OUT)

@app.route('/camera')
def cam(req,resp):
    # parse query string
    start = time.ticks_ms()
    camera.init(0, d0 = 4, d1 = 5, d2 = 18, d3 = 19, d4 = 36
                , d5 = 39, d6 = 34, d7 = 35
                , format=camera.JPEG, framesize=camera.FRAME_VGA
                , xclk = 21, pclk = 22, vsync = 25, href = 23
                , siod = 26, sioc = 27, pwdn=-1, reset=-1)
    camera.quality(10)
    # wait for sensor to start and focus before capturing image
    buf = camera.capture()
    camera.deinit()
    camcap = time.ticks_ms()
    
    #f = open('image.jpg','w')
    #f.write(buf)
    #f.close()
    #endw = time.ticks_ms()
    
    if len(buf) > 0:
        yield from picoweb.start_response(resp, "image/jpeg")
        #file = open('image.jpg','rb')
        responce = buf #file.read()
        #file.close()
        yield from resp.awrite(responce)
        end = time.ticks_ms()
        print(time.ticks_diff(camcap,start))
        #print(time.ticks_diff(endw,camcap))
        print(time.ticks_diff(end,camcap))
        print(time.ticks_diff(end,start))


    else:
        picoweb.http_error(resp, 503)


@app.route('/')
def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("Hello world from picoweb running on the ESP32")

def run():
    app.run(host='192.168.1.178', port=80, debug=True)
    
run()