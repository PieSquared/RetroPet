import os
import random
import time

from gpiozero import Button
from luma.core.interface.serial import spi
from luma.lcd.device import ili9341
from PIL import Image

BUTTON_PIN = 17
DC_PIN = 24
RESET_PIN = 25

SHEET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sprites.png")
FACES = ["neutral", "happy", "wink", "smug", "sad", "angry", "surprised", "sleepy", "love"]
FPS = 4


def load_faces():
    sheet = Image.open(SHEET).convert("RGBA")
    faces = {}
    for r, name in enumerate(FACES[:sheet.height // 60]):
        frames = []
        for c in range(sheet.width // 80):
            cell = sheet.crop((c * 80, r * 60, (c + 1) * 80, (r + 1) * 60))
            if cell.getchannel("A").getbbox() is None:   # blank cell
                continue
            img = Image.alpha_composite(Image.new("RGBA", (80, 60), (0, 0, 0, 255)), cell).convert("RGB")
            frames.append(img.resize((320, 240), Image.NEAREST))
        if frames:
            faces[name] = frames
    return faces


faces = load_faces()
moods = list(faces)

serial = spi(port=0, device=0, gpio_DC=DC_PIN, gpio_RST=RESET_PIN, bus_speed_hz=32_000_000)
screen = ili9341(serial, width=320, height=240)

presses = 0


def pressed():
    global presses
    presses += 1


button = Button(BUTTON_PIN, bounce_time=0.05)
button.when_pressed = pressed

on = True
face = moods[0]
face_start = time.monotonic()
next_change = face_start + 8
shown = None

print("running")
try:
    while True:
        t = time.monotonic()

        while presses:
            presses -= 1
            on = not on
            if on:
                screen.show()
            else:
                screen.display(Image.new("RGB", (320, 240), (0, 0, 0)))
                screen.hide()
            shown = None
            face_start = t
            next_change = t + 8

        if on:
            if t >= next_change:
                face = random.choice([m for m in moods if m != face] or moods)
                face_start = t
                next_change = t + random.uniform(6, 14)

            frames = faces[face]
            n = int((t - face_start) * FPS) % len(frames)
            if (face, n) != shown:
                screen.display(frames[n])
                shown = (face, n)
            time.sleep(0.05)
        else:
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    screen.display(Image.new("RGB", (320, 240), (0, 0, 0)))
    screen.hide()
    button.close()
