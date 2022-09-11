from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def render(template_name: str = 'index.html', folder_path: str = 'templates', **kwargs) -> str:
    # создаем объект окружения
    env = Environment()
    # указываем папку для поиска шаблонов
    env.loader = FileSystemLoader(folder_path)
    # находим шаблон в окружении
    template = env.get_template(template_name)

    return template.render(**kwargs)
