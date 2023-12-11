
from fastapi import WebSocket, FastAPI, WebSocketDisconnect

app = FastAPI()

# This will store active WebSocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

# Instantiate the connection manager
manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Connect the client
    await manager.connect(websocket)
    try:
        while True:
            # Wait for any message from the client
            data = await websocket.receive_text()
            # Send the message to all connected clients
            await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        # Handle disconnection
        manager.disconnect(websocket)
        await manager.broadcast("Client left the chat")


