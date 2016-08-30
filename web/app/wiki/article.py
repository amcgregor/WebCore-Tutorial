class Article:
	"""A wiki article."""
	
	__dispatch__ = 'resource'
	
	def __init__(self, context, wiki, page):
		self._ctx = context  # The "request context" we were constructed for.
		self._wiki = wiki  # The parent (containing) Wiki instance.
		self._page = page  # The data associated with the page we represent.
	
	def get(self):
		return "I'm an article named " + self._page['name']
	
	def post(self, content):
		"""Update the in-database content for the current article."""
		
		return {'ok': True}  # For now, we only pretend.
	
	def delete(self):
		"""Delete this page from the wiki."""
		
		return {'ok': True}  # For now, we only pretend.

