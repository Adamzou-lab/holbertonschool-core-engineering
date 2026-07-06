#!/usr/bin/env python3
"""ASGI application serving an HTML page and a WebSocket echo endpoint."""
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    """Serve a simple HTML page."""
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    """Echo back every message received from the client."""
    await websocket.accept()
    async for message in websocket.iter_text():
        await websocket.send_text(message)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
