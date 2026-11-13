
# November 12, 2026: A Little Bit of Planning

Today I spent my time on researching what I really want/need for this project. In the images is my prototyping sheet. It's messy because I like my sheets that way, but here is a summary.

## Design Choices

I am picking between 2 different designs, a Generic vintage PC or a Macintosh look. I laid out the pros and cons of each of them and decided to use the vintage PC look because it has potential for more features.

## Hardware Ideas

Some features I thought of were:

- Battery power
- Maybe a magnetic charger
- Instead of using screws to assemble it, I use magnets

I was really thinking about the replacing screws because if it fell, it may fall into pieces depending on how many parts I would attach.

I want a few buttons on it, and maybe a knob on it for something.

## Software Ideas

On the software side, I wanted to add:

- A Spotify display, which requires a Bluetooth thing, or I could use the Spotify app API.
- A little face because its a desktop pet.
- Maybe a Google Assistant.

I was thinking about this one because I would need a microphone and a small speaker. I was thinking about taking apart an old Google Home thing I could get parts from.

## Configuration System

I would also need a way for the user to edit configs. Then I remembered a feature called RaspberryPi Connect, which I already have and made a system for.

Normally, RaspberryPi Connect requires a monitor to stream, and if you unplug the monitor, it stops. But if you add a line to the firmware that makes the Raspberry Pi think there's a monitor connected, it works without one.

I already have 2 scripts, so I could make a button combo that makes acivates it and makes it go into a config state that lets Raspberry Pi Connect turn on and off.

The reason I dont want to keep it on all the time is because it uses a lot of resources and makes heat, which also made me realize I need heatsinks on it.


**Total time spent: 0.5h**

![](https://fabricate.hackclub-assets.com/5b4d79beb641e6a5b56d679dc8b9cf140ec149d032515227a5114a8933bf00f6/image-png/image.png)
![](https://fabricate.hackclub-assets.com/cec984cc2d29b96cacb1494738dfd31f84cd6387af8c48953e67a40bbf65236a/image-png/image.png)

---


