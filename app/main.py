import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'hal'))
import hal_led as led
import hal_adc as adc
import hal_lcd as LCD
import hal_keypad as keypad

password = []

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    global lcd

    password.append(key)

    print(password)

    lcd.lcd_display_string(str(key), 2);


def main():
    print("Hello template")

    global lcd

    lcd = LCD.lcd()

    led.init()
    adc.init()
    keypad.init()

    lcd.lcd_clear()

    lcd.lcd_display_string("Hello", 1)

    led.set_output(1, 0)

    keypad.get_key(key_pressed)

    while (True):
        val = adc.get_adc_value(1)
        print(str(val) + "\n")


if __name__ == '__main__':
    main()



