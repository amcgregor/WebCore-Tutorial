# Python's standard date + time object.
from datetime import datetime

# HTTP status code exception for "302 Found" redirection.
from webob.exc import HTTPFound

# MongoDB exceptions that may be raised when manipulating data.
from pymongo.errors import DuplicateKeyError

# Get a reference to our Article resource class.
from .article import Article


class Wiki:
	"""Basic multi-article editable wiki."""
	
	__dispatch__ = 'resource'  # The Wiki is a collection of pages, so use resource dispatch.
	__resource__ = Article  # Declare the type of resource we contain.
	__collection__ = 'articles'
	
	def __init__(self, context, collection=None, record=None):
		"""Executed when the root of the site (or children) are accessed, on each request."""
		self._ctx = context  # Store the "request context" for later use.
	
	def __getitem__(self, name):
		"""Load data for the Article with the given name."""
		
		data = self._ctx.db[self.__collection__].find_one({'_id': name})
		
		if not data:  # If no record was found, populate some default data.
			data = {
					'_id': name,
					'content': None,
					'modified': None,
				}
		
		return data
	
	def get(self):
		"""Called to handle direct requests to the web root itself."""
		
		return HTTPFound(location=str(self._ctx.path.current / 'Home'))  # Issue the redirect.
	
	def post(self, name, content):
		"""Save a new article to the database."""
		
		try:
			result = self._ctx.db[self.__collection__].insert_one({
					'_id': name,
					'content': content,
					'modified': datetime.utcnow(),
				})
		
		except DuplicateKeyError:
			return {
					'ok': False,
					'reason': 'duplicate',
					'message': "An article with that name already exists.",
					'name': name,
				}
		
		# All is well, so we inform the client.
		return {
				'ok': True,
				'acknowledged': result.acknowledged,
				'name': result.inserted_id
			}

