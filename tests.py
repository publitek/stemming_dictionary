import sys

from unittest import TestCase, TestSuite, TextTestRunner
from collections import OrderedDict
from subprocess import Popen, PIPE

## STEM TESTS
def stem_tests(*args):
    def decorator(method, args=args):
        for arg in args:
            def method_for_arg(self, method=method, arg=arg):
                method(self, *arg)
            name = method.__name__ + '(' + '->'.join(arg[:2]) + ')'
            frame = sys._getframe(1)  # pylint: disable-msg=W0212
            frame.f_locals[name] = method_for_arg
        return None
    return decorator

## STEMMING TEST CASE
class StemmingTestCase(TestCase):
    ## RUN TEST
    def stem(self, input):
        process = Popen(
            args = ['hunspell', '-m', '-d', 'en_US', '-s'],
            stdin = PIPE,
            stdout = PIPE,
        )
        (stdout, stderr) = process.communicate(input)
        return stdout.replace(input, '').strip()

    ## TEST STEMMING
    @stem_tests(
        ('men', 'man', True),
        ('women', 'woman', True),
        ('conmen', 'conman', True),
        ('congressmen', 'congressman', True),
        ('people', 'person', True),
        ('teeth', 'tooth', True),
        ('mothers', 'mother', True),
        ('telemarketer', 'telemarket', True),
        ('telemarketers', 'telemarket', True),
        ('telemarketing', 'telemarket', True),
        ('butter', 'butt', False),
        ('corner', 'corn', False),
        ('easter', 'east', False),
    )
    def test_stemming(self, input, output, equal):
        if equal:
            self.assertEqual(self.stem(input), output, 'SHOULD STEM %s -> %s'%(input, output))
        else:
            self.assertNotEqual(self.stem(input), output, 'SHOULD NOT STEM %s -> %s'%(input, output))
