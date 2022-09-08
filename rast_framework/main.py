from quopri import decodestring

from .parse_requests import GetRequests, PostRequests


class PageNotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Rust:
    """Класс Framework - основа фреймворка"""

    def __init__(self, routes: dict, fronts: list):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        # получаем адрес, по которому выполнен переход
        path = environ['PATH_INFO']

        # добавление закрывающего /
        if not path.endswith('/'):
            path = f'{path}/'

        request = {}

        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = Rust.decode_value(data)
            print(f'Нам пришёл post-запрос: {Rust.decode_value(data)}')
        if method == 'GET':
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = Rust.decode_value(request_params)
            print(f'Нам пришли GET-параметры:'
                  f' {Rust.decode_value(request_params)}')

        # находим нужный контроллер
        # отработка паттерна page controller
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()

        # наполняем словарь request элементами
        # этот словарь получат все контроллеры
        # отработка паттерна front controller
        for front in self.fronts:
            front(request)
        # запуск контроллера с передачей объекта request
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = [bytes(item.replace('%', '=').replace("+", " "), 'UTF-8') for item in v]
            val_decode: list = [decodestring(item).decode('UTF-8') for item in val]
            new_data[k] = val_decode
        return new_data
