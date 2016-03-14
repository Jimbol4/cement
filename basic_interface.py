from cement.core.foundation import CementApp
from cement.core.interface import Interface, Attribute

class MyInterface(Interface):
    class IMeta:
        label = 'myinterface'

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
