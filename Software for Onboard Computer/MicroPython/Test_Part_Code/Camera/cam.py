import camera
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
    await asyncio.sleep(2)
    buf = camera.capture()
    camera.deinit()
    print(str(buf))
    if len(buf) > 0:
        return buf
    else:    
        return "Error"

f = cam()

