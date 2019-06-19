from flask_socketio import send, emit
from app import socketio
from time import sleep

counter = 0

@socketio.on('client_connected')
def handle_client_connect_event(json):
    print('received json: {0}'.format(str(json)))

@socketio.on('message')
def handle_json_button(json, smf):
    # it will forward the json to all clients.
    send(json, json=True)


@socketio.on('alert_button')
def handle_alert_event(json):
    # it will forward the json to all clients.
    print('Message from client was {0}'.format(json))
    for i in range(10):
        emit('alert', 'Message from backend')
        sleep(1)

@socketio.on('counter')
def handle_counter(json, smf=None):
    global counter
    counter += 1
    emit('counter', counter)