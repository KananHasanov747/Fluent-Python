"""просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> tag
<function tag at 0x10086b010>
>>> from functools import partial
>>> picture = partial (tag, 'img', cls = 'pic-frame')
>>> picture (src = 'wumpus.jpeg')
'<img class = "pic-frame" src = "wumpus.jpeg" />'
>>> picture
functools.partial(<function tag at 0x10086b010>, 'img', cls='pic-frame')
>>> picture.func
<function tag at 0x10086b010>
>>> picture.args
('img',)
>>> picture.keywords
{'cls': 'pic-frame'}

"""
def tag (name, *content, cls = None, **attrs):
	"""Generating one or some HTML - tags"""
	if cls is not None:
		attrs ['class'] = cls
	if attrs:
		attr_str = ''.join (' %s = "%s"' % (attr, value)
							for attr, value
							in sorted (attrs.items ()))
	else:
		attr_str = ''
	if content:
		return '\n'.join ('<%s%s>%s</%s>' %
						  (name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)