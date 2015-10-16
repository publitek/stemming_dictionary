from subprocess import Popen, PIPE

def stem(input):
    process = Popen(
        args = ['hunspell', '-m', '-d', 'en_US', '-s'],
        stdin = PIPE,
        stdout = PIPE,
    )
    (stdout, stderr) = process.communicate(input)
    print stdout
    return stdout.replace(input, '').strip()

def test_stemming():
    with open('tests.txt') as file:
        for line in file:
            if line.startswith('#'):
                continue
            line = line.rstrip('\n').split('#')[0].strip()
            try:
                (input, output) = line.split(';')
                yield validate, input.strip(), output.strip()
            except ValueError:
                if line:
                    yield validate, line, line

def validate(input, output):
    stemmed = stem(input)
    print '%r %r'%(output, stemmed)
    assert stemmed == output or (stemmed == '' and input == output), 'input: {}, expected: {}, actual: {}'.format(input, output, stemmed)
