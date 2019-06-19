from flask_socketio import send, emit
from app import socketio
from time import sleep
from flask import request

counter = 0

players = {}

@socketio.on('connect')
def handle_client_connect_event():
    playerid = 1
    print('eee')
    emit('hi', f'playerId = {request.sid}')

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