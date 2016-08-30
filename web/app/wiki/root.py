# An easy way to safely combine paths.
from pathlib import PurePosixPath

# HTTP status code exception for "302 Found" redirection.
from webob.exc import HTTPFound

# Get a reference to our Article resource class.
from .article import Article


class Wiki:
	"""Basic multi-article editable wiki."""
	
	__dispatch__ = 'resource'  # The Wiki is a collection of pages, so use resource dispatch.
	__resource__ = Article  # Declare the type of resource we contain.
	
	def __init__(self, context, collection=None, record=None):
		"""Executed when the root of the site (or children) are accessed, on each request."""
		self._ctx = context  # Store the "request context" for later use.
	
	def __getitem__(self, name):
		"""Load data for the Article with the given name."""
		
		return {'name': name}  # We pretend, for now.
	
	def get(self):
		"""Called to handle direct requests to the web root itself."""
		
		# Identify where this wiki is attached.
		path = PurePosixPath(self._ctx.path[-1][1])
		
		return HTTPFound(location=str(path / 'Home'))  # Issue the redirect.
	
	def post(self, name, content):
		"""Save a new article to the database."""
		
		return {'ok': True}  # For now, we only pretend.

