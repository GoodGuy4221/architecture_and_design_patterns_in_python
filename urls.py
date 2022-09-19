from datetime import date
import views as view


# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/contacts/': view.Contacts(),
}

routes.update(view.routes)
