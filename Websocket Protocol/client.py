import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8080"
    async with websockets.connect(uri) as websocket:
        message = input("Enter a message to send: ")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received response: {response}")

if __name__ == "__main__":
    asyncio.run(hello())
