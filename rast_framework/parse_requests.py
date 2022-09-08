class GetRequests:

    @staticmethod
    def parse_input_data(data: str) -> dict:
        result = {}
        if data:
            # делим параметры через &
            params = data.split('&')

            if not params:
                params = data.split()

            for item in params:
                # делим ключ и значение через =
                k, v = item.split('=')
                result[k] = v
        return result

    @classmethod
    def get_request_params(cls, environ: dict) -> dict:
        # получаем параметры запроса
        query_string = environ['QUERY_STRING']
        # превращаем параметры в словарь
        request_params = cls.parse_input_data(query_string)
        return request_params


class PostRequests:

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        # получаем длину тела
        content_length_data = env.get('CONTENT_LENGTH')
        # приводим к int
        content_length = int(content_length_data) if content_length_data else 0
        print(content_length)
        # считываем данные, если они есть
        # env['wsgi.input'] -> <class '_io.BufferedReader'>
        # запускаем режим чтения

        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    @staticmethod
    def parse_wsgi_input_data(data: bytes, get_parse=GetRequests()) -> dict:
        result = {}
        if data:
            # декодируем данные
            data_str = data.decode(encoding='utf-8')
            print(f'строка после декод - {data_str}')
            # собираем их в словарь
            result = get_parse.parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        # получаем данные
        data = self.get_wsgi_input_data(environ)
        # превращаем данные в словарь
        data = self.parse_wsgi_input_data(data)
        return data
