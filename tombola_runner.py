# 11.15

import doctest

from tombola import Tombola

# модули, подлежащие тестированию
import bingo, lotto, tombolist, drum

TEST_FILE = 'tombola.tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'

def main (argv):
	verbose = '-v' in argv
	real_subclasses = Tombola.__subclasses__ ()
	virtual_subclasses = list (Tombola._abc_registry)

	for cls in real_subclasses + virtual_subclasses:
		test (cls, verbose)

def test (cls, verbose = False):
	res = doctest.testfile (
			TEST_FILE,
			globs = {'ConcreteTombola' : cls},
			verbose = verbose,
			optionflags = doctest.REPORT_ONLY_FIRST_FAILURE)
	tags = 'FAIL' if res.failed else 'OK'
	print (TEST_MSG.format (cls.__name__, res, tag))

if __name__ == '__main__':
	import sys
	main (sys.argv)

# tombola_test.rst is sample of 11.16