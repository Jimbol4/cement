from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController

VERSION = '0.9.1'

BANNER = """
An example application v%s
""" % VERSION

class MyBaseController(CementBaseController):
	class Meta:
		label = 'base'
		description = 'MyApp Does Amazing Things'
		arguments = [
		(['-v', '--version'], dict(action='version', version=BANNER))
		]

class MyApp(CementApp):
	class Meta:
		label = 'myapp'
		base_controller = MyBaseController

with MyApp() as app:
	app.run()