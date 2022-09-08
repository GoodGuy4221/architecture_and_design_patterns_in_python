from datetime import date
from views import Index, Content, Still, About, Contacts


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/content/': Content(),
    '/still/': Still(),
    '/about/': About(),
    '/contacts/': Contacts(),
}
