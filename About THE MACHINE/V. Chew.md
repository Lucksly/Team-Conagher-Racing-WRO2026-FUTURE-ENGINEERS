V. Chew
===

This, is THE MACHINE'S evolved state, V. Chew, the changes are few but practical, mainly, he's shorter and is now programed in micropython via pybricks.

<img height="250" width="520" src="V. Chew pictures/IMG_E1810.JPG">

He measures in at 24.5 cm long, 19.5 cm wide and 10.5 cm tall he's equiped with the same wheels and electronic components as V. Juan, so they aren't that different from one another.

<table>
    <tr>
        <td>
            <img src="V. Chew pictures/IMG_E1811.JPG"> Front
        </td>
        <td>
            <img src="V. Chew pictures/IMG_E1812.JPG"> Right Side
        </td>
                <td>
        <img src="V. Chew pictures/IMG_E1813.JPG"> Rear
        </td>
    </tr>
    <tr>
        <td>
            <img src="V. Chew pictures/IMG_E1814.JPG"> Left Side 
        </td>
        <td>
            <img src="V. Chew pictures/IMG_E1815.JPG"> Top Down 
        </td>
                <td>
        <img src="V. Chew pictures/IMG_E1816.JPG"> Bottom Up
        </td>  
    </tr>
</table>

V. Chew Upgrades
===
The measurements haven't changed, although some components have been changed:

Wheels:
    
We now use 3d printed Enkei RPF1 rims for weight saving purposes which can be found [here](https://cults3d.com/en/3d-model/game/1-10-rc-rim-rpf1)

Electronics:

We have removed the Lego Spike Color Sensor due to its limited range, in its place originally there was going to be a [Cytron Maker Pi RP2040](https://www.cytron.io/p-maker-pi-rp2040-simplifying-robotics-with-raspberry-pi-rp2040) but the one we had sourced from our coach had a missing grove port, and we had attempted to use a different grove port to have [UART](https://docs.micropython.org/en/latest/reference/glossary.html#term-UART) but the GP0 pad started lifting from the side that was connected to the trace so we decided to instead use a [Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/) provided by our coach, which we might mount to the robot using Cytron's [Robo Pico](https://www.cytron.io/p-robo-pico) but also means that THE MACHINE'S full name is now S.P.P2. V. sChew, but we just call him V. Chew cause why not. Currentlly in testing we've been using the Pico2 with a [APDS-9960](https://learn.sparkfun.com/tutorials/apds-9960-rgb-and-gesture-sensor-hookup-guide/all) conmected via [I2C](https://docs.micropython.org/en/latest/library/machine.I2C.html) which was also provided by our coach although we are considering a camera so we can have higher accuracy for detecing obstacles and the parking.

Prototype:

V. Chew R(udolf), in this version of V. Chew, we have managed to get the Lego Spike Hub to communicate effectively with the [Cytron Maker Pi RP2040](https://www.cytron.io/p-maker-pi-rp2040-simplifying-robotics-with-raspberry-pi-rp2040), which now rests under the Hub, hopefully, will give it a chance at revival as a part of our machine. This version still uses our new color sensor, the [APDS-9960](https://learn.sparkfun.com/tutorials/apds-9960-rgb-and-gesture-sensor-hookup-guide/all). Besides that, we've called this prototype version of V. Chew, V. Chew R(udolf) 'cause the [APDS-9960](https://learn.sparkfun.com/tutorials/apds-9960-rgb-and-gesture-sensor-hookup-guide/all) color sensor, which is RED, is placed right in the front of our distance sensor, makin' it look like a Rudolf's nose. The reason we put the color sensor there is to make use of the distance sensor's LED light to further increase our color sensor's accuracy.
<img height="250" width="520" src="/V. Chew pictures/IMG_1626.JPG">

