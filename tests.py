from subprocess import Popen, PIPE

def stem(input):
    process = Popen(
        args = ['hunspell', '-m', '-d', 'en_US', '-s'],
        stdin = PIPE,
        stdout = PIPE,
    )
    (stdout, stderr) = process.communicate(input)
    return stdout.replace(input, '').strip()

STEMS = []
with open('test_data.txt') as file:
    for line in file:
        if line.startswith('#'):
            continue
        line = line.rstrip('\n')
        parts = line.split(';')
        if len(parts) < 2:
            STEMS.append((parts[0], parts[0]))
        else:
            STEMS.append((parts[0], parts[1]))

def test_stemming():
    for (input, output) in STEMS:
        yield validate, input, output

def validate(input, output):
    stemmed = stem(input)
    assert stemmed == output or (stemmed == '' and input == output), 'input: {}, expected: {}, actual: {}'.format(input, output, stemmed)
