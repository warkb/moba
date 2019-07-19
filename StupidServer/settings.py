"""
Файл с настройками приложения
"""
import os
import sys

PORT = os.getenv('PORT') # порт на котором запускается сервер
PORT = PORT if PORT != None else 8800
DEBUG = os.getenv('DEBUG') # находимся ли мы в режиме отладки
DEBUG = DEBUG != None
FULL_STATIC_DIR = os.path.dirname(sys.argv[0])