from wsgiref.simple_server import make_server

from rast_framework.main import Rust
from urls import routes, fronts

app = Rust(routes, fronts)

with make_server('', 5194, app) as httpd:
    print(f'Запуск на 127.0.0.1:{httpd.server_port}')
    httpd.serve_forever()
