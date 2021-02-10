import asyncio
import sys

import aioredis
import msgpack


async def main(host: str, endpoint: str, message: str):
    msg = msgpack.packb(
        {
            "endpoint": endpoint,
            "headers": {"Content-Type": "text/json"},
            "payload": message.encode("utf-8"),
        },
    )
    redis = await aioredis.create_redis_pool(host)
    await redis.rpush("acapy.outbound_transport", msg)


if __name__ == "__main__":
    args = sys.argv
    if len(args) <= 1:
        raise SystemExit("Pass redis host URL as the first parameter")
    if len(args) <= 2:
        raise SystemExit("Pass endpoint as the second parameter")
    if len(args) <= 3:
        raise SystemExit("Pass message contents as the third parameter")
    asyncio.get_event_loop().run_until_complete(main(args[1], args[2], args[3]))
