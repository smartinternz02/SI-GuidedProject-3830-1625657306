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
    m=cmd.data['command']


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    water_level=random.randint(0,100)
    intensity=random.randint(0,100)
    myData={'water_level':water_level, 'intensity':intensity}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
