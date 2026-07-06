#!/usr/bin/env python3
"""WebSocket server that validates incoming messages."""
import asyncio
import websockets


async def connection_handler(websocket):
    """Validate each message and respond accordingly."""
    async for message in websocket:
        if not message.strip():
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{message}")


async def main():
    """Start the WebSocket server on localhost:8765."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
