class Article:
	"""A wiki article."""
	
	__dispatch__ = 'resource'
	
	def __init__(self, context, wiki, page):
		self._ctx = context  # The "request context" we were constructed for.
		self._wiki = wiki  # The parent (containing) Wiki instance.
		self._page = page  # The data associated with our current Wiki page.
	
	def get(self):
		return "I'm an article named " + self._page['name']

