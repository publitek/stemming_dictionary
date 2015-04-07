from unittest import TestCase, TestSuite, TextTestRunner
from collections import OrderedDict
from subprocess import Popen, PIPE

## STEMMING TEST CASES
SHOULD_STEM = [
    ('men', 'man'),
    ('women', 'woman'),
    ('conmen', 'conman'),
    ('congressmen', 'congressman'),
    ('people', 'person'),
    ('teeth', 'tooth'),
    ('moth', ''),
    ('mothers', 'mother'),
    ('telemarketer', 'telemarket'),
    ('telemarketers', 'telemarket'),
    ('telemarketing', 'telemarket'),
]
SHOULD_NOT_STEM = [
    ('butter', 'butt'),
    ('corner', 'corn'),
    ('easter', 'east'),
]

## STEMMING TEST CASE
class StemmingTestCase(TestCase):
    ## INIT
    def __init__(self, input, expected, equal=True):
        self.input, self.expected, self.equal = input, expected, equal
        super(StemmingTestCase, self).__init__()
    ## RUN TEST
    def runTest(self):
        process = Popen(
            args = ['hunspell', '-m', '-d', 'en_US', '-s'],
            stdin = PIPE,
            stdout = PIPE,
        )
        (stdout, stderr) = process.communicate(self.input)
        base = stdout.replace(self.input, '').strip()
        if self.equal:
            self.assertEqual(base, self.expected)
        else:
            self.assertNotEqual(base, self.expected)
    ## STR
    def __str__(self):
        connector = '==' if self.equal else '!='
        return '"%s" %s "%s"'%(self.input, connector, self.expected)

## TEST SUITE
def suite():
    suite = TestSuite()
    suite.addTests(StemmingTestCase(input, expected, True) for input, expected in SHOULD_STEM)
    suite.addTests(StemmingTestCase(input, expected, False) for input, expected in SHOULD_NOT_STEM)
    return suite

## RUN
if __name__ == '__main__':
    runner = TextTestRunner(
        verbosity = 2,
    )
    runner.run(
        test = suite(),
    )
