'''просто запустите программу через command + B (для Mac),
или ctrl + B (для Windows)
И введите это:

>>> import inspect
>>> sig = inspect.signature (tag)
>>> ma_tag = {'name': 'img', 'title': 'Sunset Boulevard',
			  'src': 'sunset.jpg', 'cls': 'framed'}
>>> bound_args = sig.bind (**my_tag)
>>> bound_args
<BoundArguments (name='img', cls='framed', attrs={'title': 'Sunset Boulevard', 'src': 'sunset.jpg'})>
>>> for name, value in bound_args.arguments.items ():
...		print (name, '=', value)
name = img
cls = framed
attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
>>> del my_tag ['name']
>>> bound_args = sig.bind (**my_tag)
Traceback (most recent call last):
...
TypeError: missing a required argument: 'name'

'''

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