# HTTP status code exception for "302 Not Found" redirection.
from webob.exc import HTTPFound


class Wiki:
	"""Basic multi-article editable wiki."""
	
	def __init__(self, context=None):
		pass  # We don't use the context at all.
	
	def __call__(self):
		"""Called to handle direct requests to the web root."""
		return HTTPFound(location='/Home')  # Redirect

