from cement.core.foundation import CementApp
from cement.core.interface import Interface, Attribute

def my_validator(klass, obj):
    members = [
    '_setup',
    'do_something',
    'my_var'
    ]
    interface.validate(MyInterface, obj, members)

class MyInterface(Interface):
    class IMeta:
        label = 'myinterface'
        validator = my_validator

    Meta = Attribute('Handler Meta-data')
    my_var = Attribute('A variable of epic proportions.')

    def _setup(app_obj):
        """
        The setup function is called during application initialization and
        must 'setup' the handler object making it ready for the framework
        or the application to make further calls to it.

        Required Arguments:

            app_obj
                The application object.

        Returns: n/a

        """

    def do_something():
        """
        This function does something.
        """

class MyApp(CementApp):
    class Meta:
        label = 'myapp'
        define_handlers = [MyInterface]
