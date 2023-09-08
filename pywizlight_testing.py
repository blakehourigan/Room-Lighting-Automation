import asyncio
from pywizlight import wizlight, PilotBuilder

LEFT_BATHROOM = "192.168.1.20" 
RIGHT_BATHROOM = "192.168.1.21"

DESK = "192.168.1.11"
NIGHTSTAND  = "192.168.1.12"

all_lights = [LEFT_BATHROOM, RIGHT_BATHROOM, DESK, NIGHTSTAND]

async def toggle_light():
    light = wizlight(DESK)
    # if button pushed and previous state = off then turn them on 
    await light.updateState()
    if light.status:
        for element in all_lights: 
            light = wizlight(element)
            await light.turn_off()

    # if button pushed and previous state = on then turn them off
    else: 
        for element in all_lights: 
            light = wizlight(element)
            await light.turn_on(PilotBuilder(brightness=255))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(toggle_light())