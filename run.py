# Get a reference to the Application class.
from web.core import Application

# Get references to framework extensions.
from web.ext.annotation import AnnotationExtension
from web.ext.debug import DebugExtension

# Get a reference to our Wiki root.
from wiki.wiki import Wiki


# This is our WSGI application instance.
app = Application(Wiki, extensions=[
		AnnotationExtension(),
		DebugExtension(),
	])


# If we're run as the "main script", serve our application over HTTP.
if __name__ == "__main__":
	app.serve('wsgiref')

