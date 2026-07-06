#!/usr/bin/env python3
"""WebSocket client that sends one message to the echo server."""
import asyncio
import websockets


async def connect_and_send():
    """Send a single message and print the server's response."""
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello WebSocket")
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(connect_and_send())
