---
title: "RetroPet!!!!!"
github: "https://github.com/PieSquared/RetroPet"
description: "A Desktop pet shaped like a vintage pc with a touchscreen screen powered by a rasberry pi 3b"
created_at: "2026-11-12"
total_time: "12h"
---

# November 12, 2026: Lil bit of planning the project
<!-- fabricate:entry 2791 -->

## November 12, 2026: A Little Bit of Planning

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

---


![](https://fabricate.hackclub-assets.com/5b4d79beb641e6a5b56d679dc8b9cf140ec149d032515227a5114a8933bf00f6/image-png/image.png)
![](https://fabricate.hackclub-assets.com/cec984cc2d29b96cacb1494738dfd31f84cd6387af8c48953e67a40bbf65236a/image-png/image.png)

**Total time spent: 30m**

# November 13, 2026: Planned out what parts I need
<!-- fabricate:entry 2953 -->

---

## November 13, 2026: Figuring out what parts I need

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

![](https://fabricate.hackclub-assets.com/81fafac64259481d4314749ebabb1e16644a83e4898ae9a7455274093c9e6d58/image-png/image.png)


---

**Total time spent: 1h 30m**

# November 14, 2026: Making the case part 1
<!-- fabricate:entry 3032 -->

---

## November 14, 2026: Building the case part 1

## What I did

I didn't do that much but I did change some design choices, instead of putting the button on the front i put it on the side because it was too big annd took too much space. I also removed the knob and now we only have a button. The reason I did this is because there is no point of having buttons because we have a touch screen. I am almost done the whole case I just need to add some details and the cutout for the screen and I should be all done. This process was not that hard for me as I have done this before on On shape. The only part that was annoying was trying to find measurements for parts like the screen, the button and the rpi were easy because I have them on hand and there are plenty of 3d models, but the screen didn't have measurements online so I had to guess it, hopefully tomorrow I could maybe find a screen with measurements on them but for now I got to stick with it.

## Tomorrow

Tomorrow I just need to finish the case, add details and figure out the screen stuff. I think the project will be easy to assemble because I designed it so a 5 year old could build it. I think I will get it printed from JLCPCB because their prices are hella cheap.


![](https://fabricate.hackclub-assets.com/424fc981f44396fc088f7c4d5482d0834816578a8513b5b600acdc1c9fd6ff5b/image-png/image.png)
![](https://fabricate.hackclub-assets.com/42bd7617e60e1b487b4bb1764c98c2fd851c34756a01d464a5c76f527b4751eb/image-png/%7BCD1472A9-E3AE-47BC-953D-F2B0982850B8%7D.png)



---

**Total time spent: 3h 30m**

# November 15, 2026: Finishing the case
<!-- fabricate:entry 3142 -->

## November 15, 2026: Finishing the Case

## What I did

Today I finished the case and added a ton of details to it, I also made the cutouts to insert the magnets, i changed the magnet size from 5mm to 3mm which is pretty tiny but its because i don't want everything to be too thick. Also about the screen, I messaged the seller and she told me the exact dimensions of the screen and the entire board so I edited the model and fixed it up. For the details, I looked at a reference of a real vintage computer and took inspo. I added my own logo on it and exported it, after this journal I am going to upload everything to my github.

## Tomorrow

Tomorrow I write the firmware for it and send it out for checking or something.


![](https://fabricate.hackclub-assets.com/2c852909743bf51b8bf11db826d676b9c3587011457172c65b401dfd99724471/image-png/%7BB4B72424-B3B8-47E6-BF61-BCC87A17FC60%7D.png)
![](https://fabricate.hackclub-assets.com/830310a688806d2ddb509ecc8e73a9c1c1573a0a4f7b9748997cd68da9bd3cd8/image-png/%7B508CCD32-4590-43B6-87D8-B4F298CA1F10%7D.png)

**Total time spent: 3h 30m**

# November 16, 2026: Finishing the project
<!-- fabricate:entry 3242 -->

## November 16, 2026

## What I did

Today I did the firmware and all the stuff I need for this project to be approved, the firmware right now is basic, only including the face thing but when I get the parts for it I can add all the features. I added a thing that allows custom sprites for the faces and I might make a tool that lets users easily make the sheets because they have to be in a very specific format and have set emotions. This project is very expensive because of the RasberryPi (which I already have) and the 3D printing. If someone were to make this I would probably print it from a local print farm, but it may droop because of how bad i made one of the parts, the walls are kind of thin too so... Anyway I made a BOM.csv, a README.md, a wire diagram and a Tutorials page where it teaches the user how to set stuff up, its not like anyones gonna make this tho.

I am going to ship this right now after I am done making the journal so thanks for being part of the journey whoever is reading these lol


![](https://fabricate.hackclub-assets.com/c6148f19fa2c3dbd4920b06dfb561f3b692600459396aa436e2858576b36c399/image-png/image.png)

**Total time spent: 3h**
