from subprocess import Popen, PIPE

import asyncio


class StemmingTester:
    @staticmethod
    async def stem(inp):
        process = Popen(
            args=['hunspell', '-m', '-d', 'en_US', '-s'],
            stdin=PIPE,
            stdout=PIPE,
        )
        stdout, stderr = process.communicate(inp.encode('utf-8'))
        return stdout.decode('utf-8').replace(inp, '').strip()

    async def validate(self, input, output):
        stemmed = await self.stem(input)
        if not (stemmed == output or (stemmed == '' and input == output)):
            print('input: {}, expected: {}, actual: {}'.format(input, output, stemmed))

    async def test(self):
        tasks = []
        with open('tests.txt') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                line = line.rstrip('\n').split('#')[0].strip()
                try:
                    inp, output = line.split(';')
                except ValueError:
                    inp, output = line, line

                tasks.append(asyncio.ensure_future(self.validate(inp, output)))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    tester = StemmingTester()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tester.test())
    loop.close()
