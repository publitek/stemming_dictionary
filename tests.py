"""Tests the effectiveness of the expanded library using tests.txt"""
from multiprocessing.pool import Pool
from subprocess import Popen, PIPE


def stem(inp):
    """
    Calls the hunspell executable with the given input
    :param inp: Word to give to hunspell
    :return: Stem returned by hunspell
    """
    process = Popen(
        args=['hunspell', '-m', '-d', 'en_US', '-s'],
        stdin=PIPE,
        stdout=PIPE,
    )
    stdout, stderr = process.communicate(inp.encode('utf-8'))
    return stdout.decode('utf-8').replace(inp, '').strip()


def validate(line):
    """
    Test a given line
    :param line: The line to test
    :returns: (Result [bool], Error message [str])
    """
    if line.startswith('#'):
        return

    line = line.rstrip('\n').split('#')[0].strip()
    try:
        _input, output = line.split(';')
    except ValueError:
        _input, output = line, line

    stemmed = stem(_input)
    assertion = stemmed == output or (stemmed == '' and _input == output)
    output_str = 'input: {}, expected: {}, actual: {}'.format(_input, output, stemmed)
    return assertion, output_str


def assert_output(assertion, output_str):
    """
    Perform the assert call inside a method so yield can be used
    :param assertion: Bool to be asserted
    :param output_str: Error string if assertion fails
    """
    assert assertion, output_str


def test_stemming():
    """Runs a test for every line in tests.txt"""
    with open('tests.txt') as file:
        pool = Pool(4)
        results = pool.map(validate, file)
    for result in results:
        if result:
            yield assert_output, result[0], result[1]
