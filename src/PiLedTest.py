# System imports
import socket
import time
from time import sleep


# Local imports

#from ..hal import hal_dc_motor as dc_motor


from hal import hal_led as led
from hal import hal_input_switch as switch
import version as ver

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)





def main():
    # Instantiate and initialize the LCD driver
    # lcd = LCD.lcd()
    #
    # sleep(0.5)
    # lcd.backlight(0)  # turn backlight off
    #
    # sleep(0.5)
    # lcd.backlight(1)  # turn backlight on
    #
    # lcd.lcd_clear()
    # lcd.lcd_display_string("DevOps for AIoT", 1)  # write on line 1
    # lcd.lcd_display_string("Rel = " + ver.rel_ver, 2)  # write on line 2
    # # starting on 3rd column
    #
    # sleep(2)  # wait 2 sec
    #
    # # Get IP address
    # local_ip_address = socket.gethostbyname("raspberrypi")
    #
    # # Buzzer beep
    # buzzer.init()
    # buzzer.short_beep(0.1)
    switch.init()
    led.init()
    while(1):
        if switch.read_slide_switch() == 1:
            blink_led(0.05)
        elif switch.read_slide_switch() == 0:
            for i in range(0, 5):
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)
            while switch.read_slide_switch() == 0:
                led.set_output(0, 0)






# Main entry point
if __name__ == "__main__":
    main()