import subprocess

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
]
## TEST STEMMING
def test_stemming():
    for (input, output, equal) in STEMS:
        yield check_stem, input, output, equal
## CHECK STEM
def check_stem(input, output, equal):
    if equal:
        assert stem(input) == output, 'SHOULD STEM %s -> %s'%(input, output)
    else:
        assert stem(input) <> output,'SHOULD NOT STEM %s -> %s'%(input, output)
## STEM
def stem(input):
    process = subprocess.Popen(
        args = ['hunspell', '-m', '-d', 'en_US', '-s'],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
    )
    (stdout, stderr) = process.communicate(input)
    return stdout.replace(input, '').strip()