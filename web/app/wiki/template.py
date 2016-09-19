# encoding: cinje

: from cinje.std.html import page

: def render context, article, doc
: using page doc.name
: classes = {'wiki'}

: if not doc.content
	: classes.add('placeholder')
: end

<article&{class_=classes}>
	#{doc.content or "<i>No content.</i>"}
</article>

