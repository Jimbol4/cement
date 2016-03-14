from cement.core.foundation import CementApp
from cement.core.handler import CementBaseHandler
from basic_interface import MyInterface

class MyHandler(CementBaseHandler):
    class Meta:
        interface = MyInterface
        label = 'my_handler'
        description = 'This handler implements MyInterface'
        config_defaults = dict(foo = 'bar')

    my_var = 'This is my var'

    def __init__(self):
        self.app = None

    def _setup(self, app_obj):
        self.app = app_obj

    def do_something(self):
        print("Doing work!")

class MyApp(CementApp):
    class Meta:
        label = 'myapp'
        handlers = [MyHandler]
