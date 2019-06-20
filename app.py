from flask import Flask
from flask_socketio import SocketIO, emit
from time import sleep

players = {}




app = Flask(__name__)

def send_all_players():
      with app.app_context():
          while True:
              sleep(1 / 30)
              emit('regular_msg',
                   [player.get_dict() for player in players.values()],
                   broadcast=True,
                   namespace='/')

socketio = SocketIO(app, async_handlers=True, 
	ping_interval=0.1, ping_timeout=0.5)
socketio.start_background_task(send_all_players)

from views import index

from websockets import (
      handle_client_connect_event,
)