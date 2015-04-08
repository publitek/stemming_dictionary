from subprocess import Popen, PIPE
from operator import eq, ne

## STEM
def stem(input):
    process = Popen(
        args = ['hunspell', '-m', '-d', 'en_US', '-s'],
        stdin = PIPE,
        stdout = PIPE,
    )
    (stdout, stderr) = process.communicate(input)
    return stdout.replace(input, '').strip()
## STEMMING TESTS
STEMS = [
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
    ## (BEER,BEING) -> BEE
    ('beers', 'beer', True),
    ('beer', 'bee', False),
    ('being', 'bee', False),
]
## TEST STEMMING
def test_stemming():
    for (input, output, equal) in STEMS:
        yield validate, input, output, equal
## VALIDATE
def validate(input, output, equal):
    assert (eq if equal else ne)(stem(input), output)
