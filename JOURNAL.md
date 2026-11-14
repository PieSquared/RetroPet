
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

---

# November 13, 2026: Figuring out what parts I need

Today I just spent my time resarching and making a list of what parts I would need

## What i did i do

I looked on sites like:

- Amazon
- AliExpress
- Walmart??

AliExpress had all the parts I needed

It was really hard to find a touchscreen display that had the size I wanted, I decided on getting a 3.2 inch TFT. I wanted my screen to be big enough but not as big as the rasberrypi itself. The RPi is around 4 inches diagonally while the screen is 3.2 so I thought it would be a good fit. I needed a microphone and speaker for the google assistant addition which got me into a bit of a loop. I wated it to be portable while also being easy to assemble. I decided on using a random bluetooth speaker in my house and a tiny usb microphone. This setup makes the setup not as portable as I wanted it to but I might make the google assistant thing optional because I already have one, but still give users the option to have one. The rest of the parts were super easy to figure out, I just needed some f-f, m-f, and m-m jumper wires, buttons which I already have and a potentiometer which I also have. I want this build to be solderless so its super easy for beginners because when i tried my first soldering project it completely failed and I ended the day burning myself like 5 times. I think it would be pretty cheap to make this project, other than the RPI part which is like 35 USD which takes most of my cost, but I have it already so its fine :)

## Tomorrow?

Tomorrow I think I am going to work on the case, hopefully it will be simple but Im scared about desinging the actual monitor part because it looks complicated to print and design, I probably need to get it professionally printed. I am thinking about getting it printed from JLCPCB and using SLA resin because its cheap and pretty durable.

**Total time spent: 1.5h**

![](https://fabricate.hackclub-assets.com/81fafac64259481d4314749ebabb1e16644a83e4898ae9a7455274093c9e6d58/image-png/image.png)

---



