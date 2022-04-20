# borg-disco-cube
This is a mod of an interlocking brick set, adding colors, python and buttons to it. Enjoy

# Idea

Let's see how it looks, when the borg queen give a party, can it be used as a light?

# Needed

* one Borg cube [bluebrixx's model](https://www.bluebrixx.com/de/scifi/104179/Star-Trek-Borg-Kubus-BlueBrixx-Pro) could work
* several transparent plate brick plates, here [big ones](https://www.bluebrixx.com/de/assortments/401133/Brix-Grosse-Plates-gemischt-transparent-Trans-Clear-BlueBrixx) and [small ones](https://www.bluebrixx.com/de/assortments/401132/Brix-Lange-Plates-gemischt-transparent-Trans-Clear-BlueBrixx) were taken
* one micro controller, [xiao](https://www.seeedstudio.com/Seeeduino-XIAO-Arduino-Microcontroller-SAMD21-Cortex-M0+-p-4426.html) works
* several neo pixels [2x 10](https://wiki.seeedstudio.com/Grove-RGB_LED_Stick-10-WS2813_Mini/)
* cables, rubber bands

# How to

1. build the set as instructed
2. once build is done, enjoy the almost the pristine art
3. now replace all 6 base plate constructions with transparent plates
4. (don't think too much about that you could have done it while assembling the model, saving you to having to touch all the little plates at least twice)
5. for the back face: build the transparent base plate in a way that a two by one hole exists
6. needle the usb c power and data through the hole
7. build a system to attach a push button to the top side of the hole
10. connect the first 10x neopixel strip to A0
11. connect the second 10x neopixel strip to A1
12. connect the push button to A2 (ignoring the pull up / pull down resistors, you are a software engineer in the end!)
13. install circuit python on the xiao
14. push the [main code file](main.py) onto the xiao
15. enjoy the green lights
16. realize, you have a button attached
17. press it several times, to wonder what the diffference between the first and the second mode is


# Where from here

SPACE!!

Also you could investigate why the brightness is set to a non 1.0 value. Additionally more lights, better animation, usb_cdc and other things could be nice.
