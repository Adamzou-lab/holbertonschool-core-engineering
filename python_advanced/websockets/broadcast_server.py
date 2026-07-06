#!/usr/bin/env python3
"""WebSocket server that broadcasts messages to all connected clients."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

CLIENTS = set()


async def connection_handler(websocket):
    """Track connected clients and broadcast every message received."""
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            for client in set(CLIENTS):
                try:
                    await client.send(f"B:{message}")
                except ConnectionClosed:
                    CLIENTS.discard(client)
    except ConnectionClosed:
        pass
    finally:
        CLIENTS.discard(websocket)


async def main():
    """Start the WebSocket server on localhost:8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
