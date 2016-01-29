from multiprocessing.pool import Pool
from subprocess import Popen, PIPE


class StemmingTester:
    @staticmethod
    def stem(inp):
        process = Popen(
            args=['hunspell', '-m', '-d', 'en_US', '-s'],
            stdin=PIPE,
            stdout=PIPE,
        )
        stdout, stderr = process.communicate(inp.encode('utf-8'))
        return stdout.decode('utf-8').replace(inp, '').strip()

    def validate(self, line):
        if line.startswith('#'):
            return

        line = line.rstrip('\n').split('#')[0].strip()
        try:
            _input, output = line.split(';')
        except ValueError:
            _input, output = line, line

        stemmed = self.stem(_input)
        if not (stemmed == output or (stemmed == '' and _input == output)):
            print('input: {}, expected: {}, actual: {}'.format(_input, output, stemmed))


if __name__ == '__main__':
    tester = StemmingTester()
    pool = Pool(4)
    with open('tests.txt') as file:
        pool.map(tester.validate, file)
