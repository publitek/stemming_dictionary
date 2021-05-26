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
    # if inp.strip().__contains__(' '):
    #     print('inp', inp)
    stdout, stderr = process.communicate(inp.encode('utf-8'))
    # print('\n\n---------------------\n\n')
    # print('inp', inp)
    # print('stdout', stdout)
    # print('decode(utf-8)', stdout.decode('utf-8'))
    # print('replace(inp, "")', stdout.decode('utf-8').replace(inp, ''))
    # print("strip()", stdout.decode('utf-8').replace(inp, '').strip())
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
    # _input = _input.strip()
    output = output.replace(',', ' ').strip()
    # output = output.strip()

    stemmed = stem(_input)
    stemmed = stemmed.strip()
    stemmed = stemmed.replace('\n', '')
    # stemmed.replace('')

    if stemmed.__contains__(' ') or stemmed.__contains__('\n'):
        print('{} has two stems, {}'.format(_input, stemmed))
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
    with open('tests.txt') as file:
        current_line = file.readline()
        i = 1
        while current_line:
            assertion, output = validate(current_line)
            if not assertion:
                info = '{}:  \t{}'.format(i, current_line.replace('\n', ''))
                info += '\n\t{}'.format(output.replace('\n', ''))
                all_errors = '{}{}\n'.format(all_errors, info)
                num_errors += 1
            current_line = file.readline()
            i = i + 1
    message = 'found {} errors\n\n'.format(num_errors)
    print(message)
    f = open("errors.txt", "w")
    f.write(message)
    f.write(all_errors)
    f.close()
