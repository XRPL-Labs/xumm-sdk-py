
import asyncio
import json
from tests.fixtures import xumm_api as test_fixtures
from xumm.util import read_json

import websockets

json_fixtures = read_json('./tests/fixtures/xumm_api.json')


async def start_server(ws, path):
    try:
        print('MOCK SOCKET OPEN: {}'.format(ws.open))

        await ws.send(json.dumps(test_fixtures.subscription_updates()['expire']))  # noqa: E501
        print('SENT EXPIRE')
        print(test_fixtures.subscription_updates()['expire'])

        await ws.send(json.dumps(test_fixtures.subscription_updates()['opened']))  # noqa: E501
        print('SENT OPENED')
        print(test_fixtures.subscription_updates()['opened'])

        await ws.send(json.dumps(test_fixtures.subscription_updates()['rejected']))  # noqa: E501
        print('SENT REJECTED')
        print(test_fixtures.subscription_updates()['rejected'])

        await asyncio.sleep(1)

    except KeyboardInterrupt:
        ws.close()

    except Exception as e:
        print('on_open Error: {}'.format(e))
        ws.close()


async def main():
    async with websockets.serve(start_server, "localhost", 8765):
        await asyncio.Future()  # run forever


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
