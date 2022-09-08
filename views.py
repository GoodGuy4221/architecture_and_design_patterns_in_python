from rast_framework.templator import render


class Index:
    def __call__(self, request):
        context = {
            'page_title': 'Главная',
        }
        return '200 OK', render(template_name='index.html', **context)


class Content:
    def __call__(self, request):
        context = {
            'page_title': 'Контент',
        }
        return '200 OK', render('content.html', **context)


class Still:
    def __call__(self, request):
        context = {
            'page_title': 'Еще',
        }
        return '200 OK', render('still.html', **context)


class About:
    def __call__(self, request):
        context = {
            'page_title': 'Об этом',
        }
        return '200 OK', render('about.html', **context)


class Contacts:
    def __call__(self, request):
        context = {
            'page_title': 'Контакты',
        }
        return '200 OK', render('contacts.html', **context)
