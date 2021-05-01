from PyP100 import PyP100 as lamp
import sys
import reapy
import json


user = "email@address.troll"
pw = "somepassword"
ip_address = "192.168.2.130"
rec_lamp = lamp.P100(ip_address, user, pw)
rec_lamp.handshake() #Creates the cookies required for further methods 
rec_lamp.login() #Sends credentials to the plug and creates AES Key and IV for further methods
device_info = json.loads(rec_lamp.getDeviceInfo())["result"]

is_on = device_info["device_on"]
proj = reapy.Project()

def main(is_on):
    if (proj.is_paused or proj.is_stopped) and is_on:
        reapy.print("Recording paused. lamp OFF!")
        rec_lamp.turnOff()
        is_on = False
    elif proj.is_recording and not is_on:
        reapy.print("Recording lamp ON!")
        rec_lamp.turnOn()
        rec_lamp.setBrightness(100)
        is_on = True
    elif not proj.is_recording and is_on:
        reapy.print("Not Recording. lamp OFF!")
        rec_lamp.turnOff()
        is_on = False
    reapy.defer(main, is_on)

if __name__ == "__main__":
    main(is_on)
