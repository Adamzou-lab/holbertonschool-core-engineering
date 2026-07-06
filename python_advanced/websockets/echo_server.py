#!/usr/bin/env python3
"""WebSocket echo server."""
import asyncio
import websockets


async def echo(websocket):
    """Echo back every message received from a client."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server on localhost:8765."""
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
