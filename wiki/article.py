class Article:
	"""A wiki article."""
	
	def __init__(self, context, name):
		self._name = name  # Save this for later.
	
	def __call__(self):
		return "I'm an article named " + self._name

