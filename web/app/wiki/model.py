from datetime import datetime

from marrow.mongo.core import Document
from marrow.mongo import String, Date


class WikiArticle(Document):
	name = String('_id')
	content = String()
	modified = Date(default=datetime.utcnow, assign=True)

