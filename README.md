# Physics Experiments

## Objectives and Motivation
The goal for the following projects is to use microcontrollers such as Raspberry Pi and Arduino to conduct simple Physics experiments that can be done with available sensors.

## Current Parts List 

The following is the up-to-date parts list for the experiments.

1. Raspberry Pi 4B (8GB RAM)
2. HD-SR04 Ultra Sonic Sensors
3. Measuring Tape
4. Small Staright piece of cardboard

## First Experiment: Measuring the Speed of Sound using the HD-SR04 Ultra Sonic Sensors

### How the Sensor works

In the most basic terms, the sensor has 2 "eyes". One of the eyes sends a sonic pulse towards an object. The pulse will bounce back into the other eye of the sensor. The time it takes for that pulse to be transmitted and received is collected by the Raspberry Pi. 

The sonic pulses are essentially sound waves that are traveling through a medium, such as air in this case. Under normal conditions, these sonic pulses should be traveling at around 343 meters/second. We will use the time data received and a measuring device to approximate the speed of sound. 

### The Set-Up

We will use the ultra sonic sensor that is mounted to the rover below as our sensor. 

* Insert Image Here

The range of the sensor according to the data sheet is about 4 meters. We will use a measuring tape to measure out 4 meters from the front of the towards a wall. THe sonic pulses will bounce off a cardboard that I will place in front of the rover in 10cm increments.

* Insert Image Here

### Python Program

The program in this repositiory is designed to collect the time it takes for the sonic pulses to be transmitted and received by the sensor. This number is divided by 2 since the time measurements accounts for both sending and receiving times. To be thorough in our approach and to ensure consistent data points, the program captures 1000 time measurements per 10cm intervals. These 1000 data points are averaged to get accurate results. 

### Excel Sheet

For every 10cm interval, the python program returns how long it took the pulse to hit the cardboard box. I wrote these time measurements within an excel sheet and used the distance and time data to calculate the speed of the pulse. (Speed = Distance/Time)

## Analysis


