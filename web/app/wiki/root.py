# HTTP status code exception for "302 Found" redirection.
from webob.exc import HTTPFound


class Wiki:
	"""Basic multi-article editable wiki."""
	
	def __init__(self, context):
		"""Exeuted when the root of the site (or children) are accessed, on each request."""
		self._ctx = context  # Store the "request context" for later use.
	
	def __call__(self):
		"""Called to handle direct requests to the web root itself."""
		return HTTPFound(location='/Home')  # Issue the redirect.

