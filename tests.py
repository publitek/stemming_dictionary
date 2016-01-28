from subprocess import Popen, PIPE

import asyncio


class StemmingTester:
    @staticmethod
    def stem(inp):
        process = Popen(
            args=['hunspell', '-m', '-d', 'en_US', '-s'],
            stdin=PIPE,
            stdout=PIPE,
        )
        stdout, stderr = process.communicate(inp)
        return stdout.replace(inp, ''.encode('UTF-8')).strip()

    async def validate(self, input, output):
        stemmed = self.stem(input)
        if not (stemmed == output or (stemmed == '' and input == output)):
            print('input: {}, expected: {}, actual: {}'.format(input, output, stemmed))

    async def test(self):
        with open('tests.txt') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                line = line.rstrip('\n').split('#')[0].strip()
                try:
                    inp, output = line.split(';')
                    self.validate(inp.strip(), output.strip())
                except ValueError:
                    if line:
                        self.validate(line, line)


if __name__ == '__main__':
    tester = StemmingTester()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tester.test())
    loop.close()
