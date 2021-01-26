import asyncio
import urllib
import sys

import aiohttp
import aioredis
import msgpack


def log_error(*args):
    print(*args, file=sys.stderr)


async def main(host: str):
    redis = await aioredis.create_redis_pool(host)
    http_client = aiohttp.ClientSession(cookie_jar=aiohttp.DummyCookieJar())
    print("Listening for messages..")
    while True:
        (_, msg) = await redis.blpop("acapy.outbound_transport")
        msg = msgpack.unpackb(msg)
        if not isinstance(msg, dict):
            log_error("Received non-dict message")
        elif b"endpoint" not in msg:
            log_error("No endpoint provided")
        elif b"payload" not in msg:
            log_error("No payload provided")
        else:
            headers = msg.get(b"headers") or {}
            endpoint = msg[b"endpoint"].decode("utf-8")
            payload = msg[b"payload"]
            parsed = urllib.parse.urlparse(endpoint)
            if parsed.scheme == "http" or parsed.scheme == "https":
                print(f"Dispatch message to {endpoint}")
                await http_client.post(endpoint, data=payload, headers=headers)
            else:
                log_error(f"Unsupported scheme: {parsed.scheme}")


if __name__ == "__main__":
    args = sys.argv
    if len(args) <= 1:
        raise SystemExit("Pass redis host URL as the first parameter")
    asyncio.get_event_loop().run_until_complete(main(args[1]))
