from unittest import TestCase, TestSuite, TextTestRunner
from collections import OrderedDict
from subprocess import Popen, PIPE

## STEMMING TEST CASES
TEST_CASES = [
    ('men', 'man'),
    ('women', 'woman'),
    ('conmen', 'conman'),
    ('congressmen', 'congressman'),
    ('people', 'person'),
    ('teeth', 'tooth'),
    ('moth', ''),
    ('mothers', 'mother'),
]

## STEMMING TEST CASE
class StemmingTestCase(TestCase):
    ## INIT
    def __init__(self, input, expected):
        self.input, self.expected = input, expected
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
        self.assertEqual(base, self.expected)
    ## STR
    def __str__(self):
        return '"%s" -> "%s"'%(self.input, self.expected)

## TEST SUITE
def suite():
    suite = TestSuite()
    suite.addTests(StemmingTestCase(input, expected) for input, expected in TEST_CASES)
    return suite

## RUN
if __name__ == '__main__':
    runner = TextTestRunner(
        verbosity = 2,
    )
    runner.run(
        test = suite(),
    )
