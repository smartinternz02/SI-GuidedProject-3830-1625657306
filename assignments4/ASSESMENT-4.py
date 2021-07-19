import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "41458d",
        "typeId": "Krishna0607",
        "deviceId":"06072002"
    },
    "auth": {
        "token": "Krishna0607"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    print()

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
