import morpfw
from morpcc.app import App as BaseApp
from morpcc.root import Root
from morpcc import permission


class AppRoot(Root):
    pass


class App(BaseApp):
    pass


@App.path(model=AppRoot, path='/')
def get_approot(request):
    return AppRoot(request)


@App.html(model=AppRoot, template='{{cookiecutter.project_name}}/index.pt', permission=permission.ViewHome)
def index(context, request):
    return {}


@App.template_directory()
def get_template_directory():
    return 'templates'
