from fastapi import FastAPI
import socketio

sio = socketio.AsyncServer(async_mode='asgi')
app = FastAPI()
sio_app = socketio.ASGIApp(sio, app)

@sio.event
async def connect(sid, environ):
    print(f"User {sid} connected")

@sio.event
async def message(sid, data):
    print(f"Message from {sid}: {data}")
    await sio.emit('reply', {'response': f"You said: {data}"})

@sio.event
async def disconnect(sid):
    print(f"User {sid} disconnected")
app.mount('/', sio_app)
