# HTTP status code exception for "302 Not Found" redirection.
from webob.exc import HTTPFound

from .article import Article


class Wiki:
	"""Basic multi-article editable wiki."""
	
	def __init__(self, context=None):
		self._ctx = context  # We pass this during Article instantiation.
	
	def __call__(self):
		"""Called to handle direct requests to the web root."""
		return HTTPFound(location='/Home')  # Redirect
	
	def __getattr__(self, name):
		"""Look up an otherwise unknown child path."""
		return Article(self._ctx, name)

