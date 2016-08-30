# An easy way to safely combine paths.
from pathlib import PurePosixPath

# HTTP status code exception for "302 Found" redirection.
from webob.exc import HTTPFound


class Wiki:
	"""Basic multi-article editable wiki."""
	
	def __init__(self, context):
		"""Exeuted when the root of the site (or children) are accessed, on each request."""
		self._ctx = context  # Store the "request context" for later use.
	
	def __call__(self):
		"""Called to handle direct requests to the web root itself."""
		
		# Identify where this application is starting from.
		path = PurePosixPath(self._ctx.path[-1][1])
		
		return HTTPFound(location=str(path / 'Home'))  # Issue the redirect.

