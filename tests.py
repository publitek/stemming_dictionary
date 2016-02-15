from multiprocessing.pool import Pool
from subprocess import Popen, PIPE


def stem(inp):
    process = Popen(
        args=['hunspell', '-m', '-d', 'en_US', '-s'],
        stdin=PIPE,
        stdout=PIPE,
    )
    stdout, stderr = process.communicate(inp.encode('utf-8'))
    return stdout.decode('utf-8').replace(inp, '').strip()


def validate(line):
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
    assert assertion, output_str


def test_stemming():
    with open('tests.txt') as file:
        pool = Pool(4)
        results = pool.map(validate, file)
    for result in results:
        if result:
            yield assert_output, result[0], result[1]
