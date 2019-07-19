"""
Максимально примитивный сервер на aiohttp и вебсокетах
Нужен для того, чтобы был базовый пример, работающий на проде,
чтобы можно было его спокойно наращивать
TODO: Делаем простой сайт, со стилем и скриптом
"""
import sys
import os

from aiohttp import web
import webbrowser

try:
    import settings
except ImportError:
    pass

try:
    from . import settings
except ImportError:
    pass

async def index(request):
    # обработчик запроса
    with open('static/index.html', 'rb') as f:
        return web.Response(body=f.read(), content_type='text/html')


# создаем экземпляр приложения
app = web.Application()

# добавляем маршрут для главной страницы
app.router.add_get('/', index)

# добавляем маршрут для статики
app.router.add_static('/static/',
                      path=f'{os.path.dirname(sys.argv[0])}/static', name='static')

# запускаем приложение
if settings.DEBUG:
    webbrowser.register('chrome', None, webbrowser.Chrome('chrome'))
    webbrowser.get().open(f'http://127.0.0.1:{settings.PORT}')
web.run_app(app, port=settings.PORT)