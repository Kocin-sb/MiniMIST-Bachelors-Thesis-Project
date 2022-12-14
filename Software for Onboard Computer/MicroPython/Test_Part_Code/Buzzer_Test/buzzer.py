import time
import machine

# These are the notes with equivalent frequency
# https://www.blackghostaudio.com/blog/basic-music-theory-for-beginners
B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978

p14 = machine.Pin(14,machine.Pin.OUT)
# Function play is use to play sound from a list of notes
def play(pin, melodies, delays, duty):
    # Loop through the whole list
    pwm = machine.PWM(pin)
    for note in melodies:
        pwm.freq(note)
        pwm.duty(duty)
        time.sleep(delays)
    # Disable the pulse, setting the duty to 0
    pwm.duty(0)
    # Disconnect the pwm driver
    pwm.deinit()

# This is the list of notes for mario theme
# 0 denotes rest notes
mario = [
     E7, E7,  1, E7,  1, C7, E7,  1,
     G7,  1,  1,  1, G6,  1,  1,  1,
     C7,  1,  1, G6,  1,  1, E6,  1,
      1, A6,  1, B6,  1,AS6, A6,  1,
     G6, E7,  1, G7, A7,  1, F7, G7,
      1, E7,  1, C7, D7, B6,  1,  1,
     C7,  1,  1, G6,  1,  1, E6,  1,
      1, A6,  1, B6,  1,AS6, A6,  1,
     G6, E7,  1, G7, A7,  1, F7, G7,
      1, E7,  1, C7, D7, B6,  1,  1
]

# This is the list of notes for jingle bells
jingle = [
    E7, E7, E7, 1,
    E7, E7, E7, 1,
    E7, G7, C7, D7, E7, 1,
    F7, F7, F7, F7, F7, E7, E7, E7, E7, D7, D7, E7, D7, 1, G7, 1,
    E7, E7, E7, 1,
    E7, E7, E7, 1,
    E7, G7, C7, D7, E7, 1,
    F7, F7, F7, F7, F7, E7, E7, E7, G7, G7, F7, D7, C7, 1
]


# This is the list of notes for Twinkle, Twinkle Little Star
twinkle = [
    C6, C6, G6, G6, A6, A6, G6, 1,
    F6, F6, E6, E6, D6, D6, C6, 1,
    G6, G6, F6, F6, E6, E6, D6, 1,
    G6, G6, F6, F6, E6, E6, D6, 1,
    C6, C6, G6, G6, A6, A6, G6, 1,
    F6, F6, E6, E6, D6, D6, C6, 1
]

def play_twinkle():
    play(p14, twinkle, 0.6, 50)
def play_jingle():
    play(p14, jingle, 0.25, 512)

# Function to easily play the mario theme
def play_mario():
	# Play the mario theme to GPIO 23
    # with 150ms note interval
    # with a low volume
    play(p14, mario, 0.15, 50)
    
def notify1():
    buzz = [A4,A4,A4]
    play(p14,buzz,0.1,150)

def notify2():
    buzz = [A4,A4,A4]
    play(p14,buzz,0.1,100)

def notify3():
    buzz = [A4,G7]
    play(p14,buzz,0.1,200)

#play_jingle()