class Article:
	"""A wiki article."""
	
	__dispatch__ = 'resource'
	
	def __init__(self, context, wiki, page):
		self._ctx = context  # The "request context" we were constructed for.
		self._wiki = wiki  # The parent (containing) Wiki instance.
		self._page = page  # The data associated with the page we represent.
	
	def get(self):
		return self._page
	
	def post(self, content):
		"""Update the in-database content for the current article.
		
		This will create the article if one by this name doesn't already exist.
		"""
		
		result = self._ctx.db.articles.update_one(
				{'_id': self._page['_id']},  # A query identifying the document to update.
				{  # The following are the MongoDB update operations to apply to the document.
					'$set': {  # Update the page content.
							'content': content,
						},
					'$currentDate': {  # Also update the last-modified time.
							'modified': True,
						}
				}
			)
		
		if not result.matched_count:  # Nothing was updated... so let's create instead.
			return self._wiki.post(self._page['_id'], content)  # You are totally allowed to do this.
		
		return {
				'ok': True,
				'acknowledged': result.acknowledged,
				'name': self._page['_id'],
			}
	
	def delete(self):
		"""Delete this page from the wiki."""
		
		result = self._ctx.db.articles.delete_one({'_id': self._page['_id']})
		
		if not result.deleted_count:  # Nothing was deleted?  We probably didn't exist!
			return {
					'ok': False,
					'reason': 'missing',
					'message': "Cowardly refusing to delete something which does not exist.",
					'name': self._page['_id'],
				}
		
		return {
				'ok': True,
				'acknowledged': result.acknowledged,
				'name': self._page['_id'],
			}

