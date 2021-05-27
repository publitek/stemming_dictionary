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
    if line.startswith('#') or line == '':
        return True, ''

    line = line.rstrip('\n').split('#')[0].strip()
    try:
        _input, output = line.split(';')
    except ValueError:
        _input, output = line, line

    _input = _input.replace(',', ' ').strip()
    output = output.replace(',', ' ').strip()

    stemmed = stem(_input)
    stemmed = stemmed.strip().replace('\n', '')

    if stemmed.__contains__(' ') or stemmed.__contains__('\n'):
        print('{} has two stems: {}'.format(_input, stemmed))
        a, b = stemmed.split(' ')
        stemmed = a

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
    with open('tests.txt') as file:
        pool = Pool(4)
        results = pool.map(validate, file)
    for result in results:
        if result:
            yield assert_output, result[0], result[1]


if __name__ == "__main__":
    all_errors = ''
    num_errors = 0
    with open('tests.txt') as tests_file:
        current_line = tests_file.readline()
        line_num = 1
        while current_line:
            valid, output = validate(current_line)
            if not valid:
                info = '{}:  \t{}'.format(line_num, current_line.replace('\n', ''))
                # print(info)
                info += '\n\t{}'.format(output.replace('\n', ''))
                all_errors = '{}{}\n'.format(all_errors, info)
                num_errors += 1
            current_line = tests_file.readline()
            line_num = line_num + 1
    message = 'Found {} errors\n\n'.format(num_errors)
    print(message)
    output_file = open("errors.txt", "w")
    output_file.write(message)
    output_file.write(all_errors)
    output_file.close()
