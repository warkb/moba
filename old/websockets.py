from flask_socketio import send, emit
from app import socketio, players
from time import sleep
from flask import request
from json import loads, dumps
from player import Player


@socketio.on('connect')
def handle_client_connect_event():
    playerid = request.sid
    # добавляем нового пользователя
    players[playerid] = Player(0, 0, playerid)
    emit('hi', 'ok')

@socketio.on('disconnect')
def handle_disconnect():
    playerid = request.sid
    del players[playerid]

@socketio.on('new_dest_point')
def handle_movement(json):
    players[request.sid].move_to_point(json['x'], json['y'])
