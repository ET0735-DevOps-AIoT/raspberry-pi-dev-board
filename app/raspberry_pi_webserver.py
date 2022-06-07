import time

import RPi.GPIO as GPIO
from flask import Flask, render_template

from hal import hal_led as led
from hal import hal_input_switch as input_switch
from hal import hal_dc_motor as motor
from hal import hal_servo as servo
from hal import hal_usonic as usonic



app = Flask(__name__)


@app.route("/")
def index():

    templateData = {
        'title': 'ET0735 - Python Flask Raspberry Pi Demo',

    }
    return render_template('raspberry_pi.html', **templateData)




@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'ledRed':
        if action == "on":
            led.set_output(1, 1)
        elif action == "off":
            led.set_output(1, 0)

    elif deviceName == 'motor':
        if action == "on":
            motor.set_motor_speed(100)
        elif action == "off":
            motor.set_motor_speed(0)

    elif deviceName == 'servo':
        if action == "on":
            servo.set_servo_position(180)
        elif action == "off":
            servo.set_servo_position(0)


    elif deviceName == 'sensor':
        if action == "refresh":
            usonic_dist = usonic.get_distance()




    # Read Sensors Status
    buttonSts = input_switch.read_slide_switch()
    usonic_dist = usonic.get_distance()

    templateData = {
        'title': 'ET0735 - Python Flask Raspberry Pi Demo',
        'button': buttonSts,
        'usonic_dist': usonic_dist
    }

    return render_template('raspberry_pi.html', **templateData)


if __name__ == "__main__":
    led.init()
    input_switch.init()
    motor.init()
    servo.init()
    usonic.init()



    #Run Python Flask Web Server
    app.run(host='0.0.0.0', port=80, debug=True)