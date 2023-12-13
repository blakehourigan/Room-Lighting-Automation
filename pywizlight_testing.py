from pywizlight import wizlight, PilotBuilder
from rpi_rf import RFDevice
import asyncio
import json


with open('config.json') as file:
    config = json.load(file)

LEFT_BATHROOM = config['LEFT_BATHROOM']
RIGHT_BATHROOM = config['RIGHT_BATHROOM']
DESK = config['DESK']
NIGHTSTAND = config['NIGHTSTAND']

all_lights = [LEFT_BATHROOM, RIGHT_BATHROOM, DESK, NIGHTSTAND]

async def toggle_light():
    light = wizlight(DESK)
    # if button pushed and previous state = off then turn them on 
    await light.updateState()
    if light.status:
        for light in all_lights: 
            light = wizlight(light)
            await light.turn_off()

    # if button pushed and previous state = on then turn them off
    else: 
        for element in all_lights: 
            light = wizlight(element)
            await light.turn_on(PilotBuilder(brightness=255))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(toggle_light())