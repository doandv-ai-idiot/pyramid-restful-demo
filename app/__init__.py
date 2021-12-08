from pyramid.config import Configurator
from pyramid_sqlalchemy import metadata


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_sqlalchemy')
    config.add_route('todos', '/api/todos')
    config.add_route('todo', '/api/todos/{id}',
                     factory='app.domain.todo.todo_factory')
    config.scan()
    metadata.create_all()

    return config.make_wsgi_app()
