import asyncio

import fire
from aiolibgen.client import Client


async def works(base_url, ids):
    c = Client(base_url)
    try:
        await c.start()
        return await c.by_ids(ids)
    finally:
        await c.stop()


if __name__ == '__main__':
    def main(base_url, ids):
        return asyncio.get_event_loop().run_until_complete(works(base_url, ids))

    fire.Fire(main)