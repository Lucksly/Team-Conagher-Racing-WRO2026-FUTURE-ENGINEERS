V. Chew
===
*[Click here](#current-state-of-v-chew) to go to the most recent version ittereation of V. Chew

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

# V. Chew Upgrades

The measurements haven't changed, although some components have been changed:

Wheels:
    
We now use 3d printed Enkei RPF1 rims for weight saving purposes which can be found [here](https://cults3d.com/en/3d-model/game/1-10-rc-rim-rpf1)

Electronics:

We have removed the Lego Spike Color Sensor due to its limited range, in its place originally there was going to be a [Cytron Maker Pi RP2040](https://www.cytron.io/p-maker-pi-rp2040-simplifying-robotics-with-raspberry-pi-rp2040) but the one we had sourced from our coach had a missing grove port, and we had attempted to use a different grove port to have [UART](https://docs.micropython.org/en/latest/reference/glossary.html#term-UART) but the GP0 pad started lifting from the side that was connected to the trace so we decided to instead use a [Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/) provided by our coach, which we might mount to the robot using Cytron's [Robo Pico](https://www.cytron.io/p-robo-pico) but also means that THE MACHINE'S full name is now S.P.P2. V. sChew, but we just call him V. Chew cause why not. Currentlly in testing we've been using the Pico2 with a [APDS-9960](https://learn.sparkfun.com/tutorials/apds-9960-rgb-and-gesture-sensor-hookup-guide/all) conmected via [I2C](https://docs.micropython.org/en/latest/library/machine.I2C.html) which was also provided by our coach although we are considering a camera so we can have higher accuracy for detecing obstacles and the parking.

Prototype #1:

V. Chew R(udolf), in this version of V. Chew, we have managed to get the Lego Spike Hub to communicate effectively with the [Cytron Maker Pi RP2040](https://www.cytron.io/p-maker-pi-rp2040-simplifying-robotics-with-raspberry-pi-rp2040), which now rests under the Hub, hopefully, will give it a chance at revival as a part of our machine. This version still uses our new color sensor, the [APDS-9960](https://learn.sparkfun.com/tutorials/apds-9960-rgb-and-gesture-sensor-hookup-guide/all). Besides that, we've called this prototype version of V. Chew, V. Chew R(udolf) 'cause the [APDS-9960](https://learn.sparkfun.com/tutorials/apds-9960-rgb-and-gesture-sensor-hookup-guide/all) color sensor, which is RED, is placed right in the front of our distance sensor, makin' it look like a Rudolf's nose. The reason we put the color sensor there is to make use of the distance sensor's LED light to further increase our color sensor's accuracy.

<img src="V. Chew pictures/IMG_1626.JPG">

# Current state of V. Chew:

<img height=175  width=700 src="V. Chew pictures/IMG_1698.jpg">

As of right now, we have decided to ditch the APDS 9960 for a [Huskylens 1 camera](https://wiki.dfrobot.com/sen0305) for more accuracy at longer distances.

Last weigh in of V. Chew he weighed 819 grams, he's still 24.5 cm long and 19.5 cm wide, but due to where the camera is mounted he's now 19 cm tall. All in, these are all the electronics we have on V. Chew:

<table>
    <tr>
        <td>
            <img src="../component images/S.P. Hub.png"> Lego Spike Prime Hub
        </td>
        <td>
             Placed at the back of THE MACHINE atop the differential, it's the heart of our MACHINE.
        </td>
                <td>
        </td>
    </tr>
    <tr>
        <td>
            <img src="../component images/Battery.png"> Lego Spike Prime Hub Battery
        </td>
        <td>
            A lithium ion recharable battery that powers the entire robot at 7.3v for 2100mAh or 15.4Wh which we have found as enough for now
        </td>
                <td>
    </tr>
    <tr>
        <td>
            <img src="../component images/Large Technic Motor.png"> Lego Spike Prime Large Motor
        </td>
        <td>
            Placed in the middle of THE MACHINE to drive it via a technic axle connected to the differential, according to Lego, it generates 8 Ncm of torque at 135 RPM and consumes 430 mA at "maximum efficiency", thanks to the 20 tooth gear at the end of the Technic axle and the 28 tooth gear on the differential, this create an increase in torque at the expense of speed which results in the wheels getting 11.2 Ncm of torque at 96.42 RPM. 
        </td>
                <td>
    </tr><tr>
        <td>
            <img src="../component images/Medium Motor.png"> Lego Spike Prime Medium Motor
        </td>
        <td>
            This motor is placed at the front of THE MACHINE, atop the steering arms and is used for steering, it generates 3.5 Ncm of torque at 135 RPM and consumes 280mA according to Lego
        </td>
                <td>
    </tr><tr>
        <td>
            <img src="../component images/RP2040.png"> Maker Pi RP2040
        </td>
        <td>
            This is the microcontroller we have placed under the Lego Spike Prime Hub, used to interface between any non Lego sensors we might use
        </td>
                <td>
    </tr><tr>
        <td>
            <img src="../component images/ultrasonic distance sensor.png"> Lego Spike Prime Ultrasonic Distance Sensor
        </td>
        <td>
            One placed at the front and one at both left and right sides for wall detection and obstacle avoiding, it can detect objects for 200 cm and has a sample rate of 100 Hz
        </td>
                <td>
    </tr></tr>
        <td>
            <img src="../component images/Huskylens.png"> HuskyLens 1
        </td>
        <td>
            This is our newest addition to V.Chew, placed atop the steering motor for accuracy when it comes to obstacle detection and hopefully will even assist us when it come to parking.
</table>

We also have some pics of him in the sun:

<table>
    <tr>
        <td>
            <img src="V. Chew pictures/IMG_1695.jpg"> Front
        </td>
        <td>
            <img src="V. Chew pictures/IMG_1694.jpg"> Right Side
        </td>
                <td>
        <img src="V. Chew pictures/IMG_1693.jpg"> Rear
        </td>
        <td>
            <img src="V. Chew pictures/IMG_1700.jpg"> The Hub and RP2040
    </tr>
    <tr>
        <td>
            <img src="V. Chew pictures/IMG_1692.jpg"> Left Side 
        </td>
        <td>
            <img src="V. Chew pictures/IMG_1696.jpg"> Top Down 
        </td>
                <td>
        <img src="V. Chew pictures/IMG_1697.jpg"> Bottom Up
        </td>
                <td>
        <img src="V. Chew pictures/IMG_1699.jpg"> Chasis without electronic components    
    </tr>
</table>
