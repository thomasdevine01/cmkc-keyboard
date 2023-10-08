## CMKC PCB Assembly Guide


### Table of Contents

1. [Foreword](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#foreword)
2. [Required Parts](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#required-parts)
3. [Optional parts](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#optional-parts)
4. [Tools](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#tools)
5. [Minimum requirements](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#minimum-requirements)
6. [Quality of Life Improvements](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#quality-of-life-improvements)
7. [PCBs: Quick Review](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#pcbs-quick-review)
8. [Soldering: Quick Review](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#soldering-quick-review)
9. [Soldering Tips](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#soldering-tips)
10. [PCB Assembly Tasks](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#pcb-assembly-tasks)
11. [Diodes](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#diodes)
12. [uC Socket](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#uc-socket)
13. [Hardware Fix - Tying Pin 9 to Pin 4](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#hardware-fix---tying-pin-9-to-pin-4)
14. [Recommended Fix - Top Layer](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#recommended-fix---top-layer)
15. [How I did it - Bottom layer underneath socket](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#how-i-did-it---bottom-layer-underneath-socket)
16. [uC header pins](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#uc-header-pins)
17. [Stabilizers](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#stabilizers)
18. [Assembling Stabilizers](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#assembling-stabilizers)
19. [Switches](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#switches)
20. [OLED](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#oled)
21. [Demultiplexer](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#demultiplexer)
22. [Rotary Encoder](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#rotary-encoder)
23. [Soldering Sanity Check](https://github.com/thomasdevine01/cmkc-keyboard/blob/main/Docs/README.md#soldering-sanity-check)

### Foreword

This document is meant to serve as a how-to guide for assembling the CMKC PCB. At the time of writing, the first revision of the PCB design has a hardware error that we will need to correct during assembly.

All source documentation can be found: [https://github.com/thomasdevine01/cmkc\_pcb](https://github.com/thomasdevine01/cmkc_pcb)

### Required Parts

- 1 - PCB
- 67 - MX Cherry style switches
- 1 - Stabilizer Kit - [60 Kit](https://www.amazon.com/DUROCK-Stabilizers-Translucent-Keyboard-Mechanical/dp/B0B2RVN19F/ref=sr_1_3?keywords=keyboard%2Bstabilizer&qid=1696142965&sr=8-3&th=1)
- 67 - Through Hole 1N4148 Diodes
- 1 - Acrylic case switch pate
- 1 - Nice!-Nano uC
  - [Manufacturer Listed Distributors](https://nicekeyboards.com/nice-nano#find-a-store)
- 1 - CD74HC4514 Demultiplexer
  - Manufacturer's website: [https://www.ti.com/product/CD74HC4514](https://www.ti.com/product/CD74HC4514)
  - Verified Distributors: [Digikey](https://www.digikey.com/en/products/detail/texas-instruments/CD74HC4514M96/1507316), [Arrow](https://www.arrow.com/en/products/cd74hc4514m96/texas-instruments), [Mouser](https://www.mouser.com/ProductDetail/Texas-Instruments/CD74HC4514M96?qs=xFfolx0DHx3s6ILXGQ%2FrLQ%3D%3D)
- 1 inch 30 AWG wire

### Optional parts

- SSD1306 128x32 pixel OLED Display
  - Must be set up for I2C communication
- Rotary Encoder
  - With or without push button
- 24 Mill-Max [header pins](https://keebd.com/en-us/products/mill-max-low-profile-controller-pins-pack-of-25)
- Female socket

### Tools

## Minimum requirements

- Soldering Iron
- Sponge
  - Water to wet the sponge
- Steel wool pad
- At least one tube of solder
- Room with a window
- Tweezers
- Patience
- Solder wick / solder sucker
- Wire cutters
  - Flush cuts preferred

## Quality of Life Improvements

- Adjustable lamp for additional lighting
- Fan to exhaust soldering fumes
- Flux
- Thin / Precision tweezers
- Steady hands
- Thin / Pencil soldering iron tip for SMD portion

### PCBs: Quick Review

PCB is a three letter acronym standing for "Printed Circuit Board". PCBs are a convenient and efficient way to connect devices and create physical circuits. PCBs can have multiple layers, allowing for complex layouts. The CMKC PCB is a two layer PCB, example below:

![](RackMultipart20231006-1-m7hbjw_html_483efb041a21293a.png)

Essentially, copper is sandwiched between layers of a dielectric material and then "etched" to remove copper where we don't want connections and masked to leave copper where we want connections. Solder mask is applied to the outer layers so that copper is exposed only on device "pads" or places we want exposed for probing, test points, etc. Vias connect copper on different layers.

The CMKC PCB was designed using KiCAD, a free, opensource, CAD software. It is recommended to view the schematic and PCB layout when trying to figure out how things are connected.

### Soldering: Quick Review

Soldering is the process of electrically connecting two (or more) pieces of metal with a low melting point alloy. The alloy used is what is known as "solder" (pronounced "Saw-Der").

There are two main types of technologies that describe how parts connect to PCBs: through hole (THT) and Surface Mount (SMD , SMT). 99% of the parts used on the CMKC PCB are through hole, there is ONE SMD that we will need to solder down in order to make our Keyboard work.

GreatScott!, on Youtube has a pretty great soldering tutorial (IMO)
[https://www.youtube.com/watch?v=VxMV6wGS3NY](https://www.youtube.com/watch?v=VxMV6wGS3NY)

## Soldering Tips

- Be mindful of how hot your soldering iron is. You need your iron to be hot enough to melt whatever solder you use, but there is such a thing as "too hot" of an iron. Particular care should be taken when soldering the Demultiplexer and the header pins on the Nice!-nano and OLED display. These devices have sensitive electronics on them and exposing them to too much heat can damage the devices.

- Be mindful of how long you hold your iron on a given pad, ~3-5 seconds should be long enough to melt the solder and make the connection. As the copper heats up, so does the FR4 substrate holding the copper in place. It is possible to melt this substrate and detach pads from the PCB, making them very susceptible to ripping.

- Try not to breathe the smoke or get it in your eyes. It is not uncommon to get leaded solder from your local hardware store. Regardless of lead content: the chemicals in solder are toxic and should not be ingested. The smoke irritates eyes and sinuses and doesn't feel good.

### PCB Assembly Tasks

## Diodes

Soldering the diodes is probably the easiest task. We're first going to want to bend the legs of the diodes so that they're roughly spaced like the pads on the PCB.

![](RackMultipart20231006-1-m7hbjw_html_1c2d2745a0b1b709.jpg)

We're then going to put the legs of the diodes through the pads on the board.

**NOTE:** The orientation of the diode is such that the black line seen on the body of the diode matches the line on the silkscreen of the PCB. The line of the body / silkscreen resembles the cathode of the diode.

![](RackMultipart20231006-1-m7hbjw_html_d2c97115a8a4dbfa.jpg)

With the diode in place, I like to bend the legs so that it stays in place and I can "rinse and repeat" for the remaining diodes

![](RackMultipart20231006-1-m7hbjw_html_ab77c0ed91fd5558.jpg)

![image31.jpg](RackMultipart20231006-1-m7hbjw_html_278c1e43b3c7ec37.gif)

After we put all the diodes in their pads, solder them, and clip the excess.

**NOTE:** You can save the diode leg clippings and use them as socket male header pins for the uC

![](RackMultipart20231006-1-m7hbjw_html_652ed7342bf25993.jpg) ![](RackMultipart20231006-1-m7hbjw_html_e44b6da1b15a0667.jpg)

![image27.jpg](RackMultipart20231006-1-m7hbjw_html_2dee802eb5a286bb.gif)

You've now put all your diodes on the board

## uC Socket

The uC socket is pretty straight forward. We're going to place the socket pins through the pads from the bottom side of the board. ![image30.jpg](RackMultipart20231006-1-m7hbjw_html_71ddc70f33d29fee.gif)

In order to ensure that the socket doesn't fall off before we get a chance to solder it to the board, I like to use tape to hold the part in place until we solder at least one pin.

Line up the socket so that it's as straight vertically as possible and use tape to hold the socket in place.

![](RackMultipart20231006-1-m7hbjw_html_3021dfe6804ad0f1.jpg)

Solder the pins from the top side of the board. ![](RackMultipart20231006-1-m7hbjw_html_434751652ef9df4d.jpg)

You'll notice that the socket pins get pretty close to where the first two switches mount onto the board. To avoid possible fitment issues, we're going to clip pins 24 and 20 from the top side.

![](RackMultipart20231006-1-m7hbjw_html_3a0a56d7bafa0c16.jpg)

###


### Hardware Fix - Tying Pin 9 to Pin 4

On the schematic I didn't catch that our CLD1 pin is tied to pin 4 on the uC, which is a ground pin (shoutout to @Josh\_little ![](RackMultipart20231006-1-m7hbjw_html_283afa9f61a344e2.png) for catching this error.) Luckily, this is a pretty easy fix. I can't show pictures of how I would recommend fixing this, because by the time this issue was found, I had already mounted the switches and the acrylic was covering where I needed to solder. Below is the pin numbering scheme for reference

![](RackMultipart20231006-1-m7hbjw_html_65679f81d1c351ea.png)

####


#### Recommended Fix - Top Layer

You'll need to solder a piece of wire that connects pin 4 to pin 9 on the top side of the board. The consequence is that this will be visible through the acrylic, so you'll want to do as clean of a job as you can.

![](RackMultipart20231006-1-m7hbjw_html_a643554812fb17b2.png)

####


#### How I did it - Bottom layer underneath socket

I was forced to do the fix this way but I do not recommend doing this if you're new to soldering. You'll notice in the picture that I burned the plastic of the socket. It's not very easy. I took a piece of 30AWG wire ~ 1 inch long and stripped one end so that a little piece of wire was exposed. I tacked that end to pin 4. I then put solder on my tip, held the wire close to pin 9 and burned through the insulation until a solder connection was made. You must be careful not to have too much solder and short and pins together. I then wiggled the excess wire lightly until it snapped off

![](RackMultipart20231006-1-m7hbjw_html_71156fc191b73bd8.jpg)

##


## uC header pins

With the socket soldered in, I put the mill-max machine header pins into the sockets. You want the pins decently in the sockets, this will be how the uC is mounted at the conclusion of this step.

**NOTE:** DO NOT POPULATE PIN 4. THAT WILL UNDO THE HARDWARE FIX DESCRIBED ABOVE. The pictures below will show pin 4 being populated,after the bug was found the pin was removed but the pictures had already been taken and I only had one board to assemble to show these steps. This is also where you could use diode legs if you don't have the Mill-Max header pins.

![](RackMultipart20231006-1-m7hbjw_html_f49ca84b6bec5dba.png)

Next place your uC onto the pins

![](RackMultipart20231006-1-m7hbjw_html_87abb840a6ece035.jpg)

Solder the pins to the uC. Try not to use so much solder such that you end up soldering the uC to the socket .

![](RackMultipart20231006-1-m7hbjw_html_bb06b5b0801bfe32.jpg)

Once cooled, you can now remove and replace your uC during debug / assembly.

##


## Stabilizers

The stabilizers need to clip into the switch plate before you begin soldering the switches. Whether you decide to go with screw in or clip in - The keyboard supports both options so that is possible. This cannot be stressed enough, if you have screw in stabilizers and plate mount switches: the stabilizers mount to the PCB and **MUST BE INSTALLED FIRST BEFORE ANY SWITCHES.**

### Assembling Stabilizers

This is a fairly straightforward process, There are three major components to stabilizers: housing, stem, and wire. Assemble the housing, insert the stem into the housing from the bottom, and then feed the wire between the housing and the stem.

NOTE: There is a sweet spot here, it may take a couple of attempts to get it right, just pop the wire from the housing and retry.

## ![](RackMultipart20231006-1-m7hbjw_html_7ccf9c76eec425c5.png) ![](RackMultipart20231006-1-m7hbjw_html_38a20b63090450e3.png) ![](RackMultipart20231006-1-m7hbjw_html_1eefa3b33a96890.png)


##


##


##


Side Note: It is common for people to modify their stabilizers. There are two common mods you can do. The first is clipping the stems. On the bottom of the stem there is an excess of plastic, clip them and you're good. The second modification is lube, apply lube to the inside of the housing and the stem where there is motion. On the bent ends of the wire, it's common for people to apply heavy lube or a type of lube called "dielectric grease", it is not necessary but does make a difference. There are endless mods to stabilizers, check out the assembly [source](https://www.keyboard.university/guides/using-screw-in-stabilizers-7nxj6) as well as a clipping [tutorial](https://switchandclick.com/how-to-mod-your-stabilizers-band-aid-clip-and-lube/).

## Switches

Note: the following pictures do not show stabilizers. This is because circuit-dude didn't realize he needed them. He installed all of his switches, bought PCB mount stabilizers after the fact, and then had to un-solder all 67 switches in order to install the stabilizers. Don't be like circuit-dude.

The switches can be a challenge while you're getting the first couple in. I found that putting in 3 switches in a triangular pattern helped keep everything relatively where it needed to be.

You're going to place the switches through the holes in the acrylic and then solder the switch to the board. Note that you need to take off the acrylic wrap prior to doing this.

![](RackMultipart20231006-1-m7hbjw_html_5a4922c93140ed3.jpg)

You want the switches to sit as flush as possible to the acrylic. ![](RackMultipart20231006-1-m7hbjw_html_bf7bc09bd2f7596f.jpg)

Fill in all the holes, solder in all the switches, and bloom blam bow you damn near got a keyboard brother.

## OLED

The OLED is pretty straight forward. Solder the header pins through the holes and then onto the board. It only fits one way. Just remember to be conscious of the heat and not fry the OLED.

![](RackMultipart20231006-1-m7hbjw_html_8635d9719a1c11cd.jpg)

##


## Demultiplexer

The demultiplexer is the only SMD part on this board. It is a little challenging due to the pin pitch but it's doable. You do need to be careful not to heat up the pads too much so that they don't delaminate and rip off the board.

I'd start with "tinning" one pad (i.e. add solder to one pad on one corner).

![](RackMultipart20231006-1-m7hbjw_html_caad3e93664f28c7.jpg)

With a corner tinned, use some tweezers to grab the IC. Prepare to move the IC onto that pad. We're going to melt the solder on the pad you just tinned and line up all the pins with their respective pads. You can melt the solder a couple of times if you don't get it right on the first shot.

**NOTE:** The long line on the silkscreen indicates Pin 1's position. Pin one is marked with the dot on the package of the IC.

![](RackMultipart20231006-1-m7hbjw_html_56edd10208b10740.jpg)

![](RackMultipart20231006-1-m7hbjw_html_1eb523808edf9d0c.jpg)

With one corner tacked down and all the pins lined up, I like to tack a pin on the opposite corner. This makes it so the part doesn't move around while you solder the next couple pins.

![](RackMultipart20231006-1-m7hbjw_html_198b8bb4fc388e96.jpg)

Note the massive solder blob in the picture above. I'd recommend cleaning that up to avoid shorting pins while soldering the pins immediately to the right.

Proceed to solder the rest of the pins in whatever way you feel comfortable.

## Rotary Encoder

**I would put the rotary encoder on last because of its height.**

The rotary encoder is pretty straight forward. Put the pins through the holes, solder the pins to the pads, bada-bing you've got a rotary encoder knob on your board. I don't have any images of installing this :'(

VOILA, you've assembled your keyboard!.

###


### Soldering Sanity Check

There is a simple program in Firmware/PCB\_sanity\_check.py that will set up all the pins associated with the matrix and then indefinitely scan the matrix and tell you which buttons were registered as pressed. You can run this code after you install circuit-python and make sure that all of your switches register when you depress them. If they don't, things to check would be:

- Demultiplexer soldering
- Switch soldering
- Socket soldering
  - Ensure that pin 4 is not populated on the uC
  - Check that pin 4 of the socket is connected to pin 9 of the socket
  - Socket connections to PCB
- Burnt traces / ripped pads
  - This would kinda suck but is fixable, it would require soldering wires from the disconnected part(s) to somewhere else that on the net that is connected.