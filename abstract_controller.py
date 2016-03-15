from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose

class AbstractBaseController(CementBaseController):
	class Meta:
		stacked_on = 'base'
		stacked_type = 'nested'
		arguments = [
		(['-f', '--foo'], dict(help='notorious foo option'))
		]

	def _setup(self, base_app):
		super(AbstractBaseController, self)._setup(base_app)

		# common attribute that can be used in sub classes/implementations
		self.reusable_dict = dict()

	@expose(hide=True)
	def default(self):
		"""
		Shared command among implementations
		"""

		if 'some_key' in self.reusable_dict.keys():
			pass

		if self.app.pargs.foo:
			print("Foo option was passed with value: %s" % self.app.pargs.foo)

		print("Inside %s.default()" % self.__class__.__name__)


class MyAppBaseController(CementBaseController):
	"""
	Application base controller (we don't want to use our abstract controller)
	"""
	class Meta:
		label = 'base'

	@expose(hide=True)
	def default(self):
		print("Inside MyAppBaseController.default()")


# an implementation of a controller that extends the abstract
class Controller1(AbstractBaseController):
	class Meta:
		label = 'controller1'

	@expose()
	def command1(self):
		print("Inside Controller1.command1()")

# another implementation
class Controller2(AbstractBaseController):
	class Meta:
		label = 'controller2'

	@expose()
	def command2(self):
		print("Inside Controller2.command2()")


class MyApp(CementApp):
	class Meta:
		label = 'myapp'
		base_controller = 'base'
		handlers = [
		MyAppBaseController,
		Controller1,
		Controller2
		]

def main():
	with MyApp() as app:
		app.run()

if __name__ == '__main__':
	main()
