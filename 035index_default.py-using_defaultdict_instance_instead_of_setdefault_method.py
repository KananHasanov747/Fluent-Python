""" Строит индекс, отображающий слово на список его вхождений """

import sys
import re
import collections

WORD_RE = re.compile ('\w+')

# Работает, если при sys.argv [x], x = -1; 0.
index = collections.defaultdict (list)
with open (sys.argv [0], encoding = 'utf-8') as fp:
	for line_no, line in enumerate (fp, 1):
		for match in WORD_RE.finditer (line):
			word = match.group ()
			column_no = match.start () + 1
			location = (line_no, column_no)
			index [word].append (location)

# напечатать в алфавитном порядке
for word in sorted (index, key = str.upper):
	print (word, index [word])