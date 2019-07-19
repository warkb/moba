"""
Файл с настройками приложения
"""
import os

PORT = os.getenv('PORT') # порт на котором запускается сервер
PORT = PORT if PORT != None else 8800
DEBUG = os.getenv('DEBUG') # находимся ли мы в режиме отладки
DEBUG = DEBUG != None