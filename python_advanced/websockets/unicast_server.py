#!/usr/bin/env python3
"""WebSocket server that unicasts responses to the sending client."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

CLIENTS = set()


async def connection_handler(websocket):
    """Track connected clients and reply only to the sender."""
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
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
