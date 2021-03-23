from roboclaw_3 import Roboclaw
from time import sleep
import time
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt


# Front Side HRSC04 Sensor (Trigger and Echo Pins)
F_TRIG = 7 
F_ECHO = 12  

# Pins are set according to board pin numbers
GPIO.setmode(GPIO.BOARD)

# Motor Controller Configuration
address = 0x80
roboclaw = Roboclaw("/dev/ttyS0", 38400)
roboclaw.Open()


# Mainly for other sensors which will be added soon
def setup():
    GPIO.setup(11, GPIO.IN)

def obstacle_avoidance():
    d_list = []
    t_list = []
    for i in range(0,1000):
        print("distance measurement in progress")
        GPIO.setup(F_TRIG,GPIO.OUT)
        GPIO.setup(F_ECHO,GPIO.IN)
        GPIO.output(F_TRIG,False)
        time.sleep(0.01)
        GPIO.output(F_TRIG,True)

        time.sleep(0.00001) # 10us pulse
        
        GPIO.output(F_TRIG,False)
        f_pulse_start = time.time()
        timeout = f_pulse_start + 0.04
        while GPIO.input(F_ECHO) == 0 and f_pulse_start < timeout:
            f_pulse_start = time.time()
            
        f_pulse_end = time.time()
        timeout = f_pulse_end + 0.04
        while GPIO.input(F_ECHO) == 1 and f_pulse_end < timeout:
            f_pulse_end = time.time()
            
        f_pulse_duration = f_pulse_end-f_pulse_start
        forward_distance = (f_pulse_duration/2) * 34300
        distance = round((forward_distance/100),6)
        time_pulse = round((f_pulse_duration/2), 6)
        d_list.append(distance)
        t_list.append(time_pulse)
        speed = (distance / (time_pulse))
        print("Speed", speed)
        print("Forward Distance:",distance,"cm\n")
    return d_list, t_list

def time_average(d,t):
    t_ave = sum(t) / len(t)
    d_ave = sum(d) / len(d)
    return t_ave, d_ave

   
def graph(d,t):
        plt.scatter(t,d)
        plt.title("Ultra Sonic Experiment")
        plt.xlabel("Pulse Time (Seconds)")
        plt.ylabel("Distance (Meters)")
        plt.xlim((0,0.001))
        plt.show()
    
if __name__ == '__main__':
    try:
        setup()
        d,t = obstacle_avoidance()
        print(time_average(d,t))

    except KeyboardInterrupt:
        pass