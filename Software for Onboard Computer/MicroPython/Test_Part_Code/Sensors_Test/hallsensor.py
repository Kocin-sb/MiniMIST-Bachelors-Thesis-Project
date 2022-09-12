import esp32
import time

def toggle(max):
    import gc
    gc.collect()
    i = max
    while i >= 0:
        print(esp32.hall_sensor())
        time.sleep(1)
        i -= 1
        
toggle(5)