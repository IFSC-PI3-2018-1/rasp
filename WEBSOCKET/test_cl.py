#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello(nID, cor):
    async with websockets.connect(
            'ws://localhost:8765') as websocket:
        s = str([nID, cor])
        await websocket.send(s)
        
        greeting = await websocket.recv()

asyncio.get_event_loop().run_until_complete(hello())
name = input("What's your name? ")
print(name)
name = input("What's your name? ")
print(type(name))