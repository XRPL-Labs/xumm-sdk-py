
import asyncio
import xumm
from unittest.mock import Mock, patch
from tests.fixtures import xumm_api as test_fixtures
from xumm.util import read_json

import websockets
import time
import json

mock_ws = None

json_fixtures = read_json('./tests/fixtures/xumm_api.json')

# print('STARTING MOCK SERVER')
async def start_server(ws, path):
    try:
        print('MOCK SOCKET OPEN: {}'.format(ws.open))
        
        # received = await ws.recv()
        # print('RECEIVED: {}'.format(received))

        await asyncio.sleep(1)

        await ws.send(json.dumps(test_fixtures.subscription_updates()['expire']))
        print('SENT EXPIRE')

        await asyncio.sleep(1)

        await ws.send(json.dumps(test_fixtures.subscription_updates()['opened']))
        print('SENT OPENED')

        await asyncio.sleep(1)

        await ws.send(json.dumps(test_fixtures.subscription_updates()['rejected']))
        print('SENT REJECTED')

        # await ws.close()
    except KeyboardInterrupt as e:
        ws.close()
        
    except Exception as e:
        print('on_open Error: {}'.format(e))
        ws.close()


def start():
    mock_ws = websockets.serve(start_server, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(mock_ws)
    asyncio.get_event_loop().run_forever()


# start()