# encoding: cinje

: from cinje.std.html import page

: def render context, article, page
: using page page['_id']
: classes = {'wiki'}

: if not page['content']
	: classes.add('placeholder')
: end

<article&{class_=classes}>
	#{page['content'] or "<i>No content.</i>"}
</article>

