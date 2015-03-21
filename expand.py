from collections import OrderedDict

## PREFIXES
PFX = {
    'A': 're',
    'I': 'in',
    'U': 'un',
    'C': 'de',
    'E': 'dis',
    'F': 'con',
    'K': 'pro',
}

## SUFFIXES
SFX = [
    'M',
]

## MAIN
def main():
    dic = OrderedDict()
    with open('en_US.dic') as f:
        for line in f:
            try:
                word, params = line.strip().split('/')
            except ValueError:
                pass
            else:
                words = []
                for key, prefix in PFX.items():
                    if key in params:
                        params = params.replace(key, '')
                        words.append(prefix + word)
                for suffix in SFX:
                    params = params.replace(suffix, '')
                if params:
                    dic[word] = params
                    for w in words:
                        dic[w] = params
    with open('en_US.dic.new', 'w') as f:
        words = sorted(dic.keys())
        f.write('%d\n'%(len(words)))
        for word in words:
            f.write('%s/%s\n'%(word, params))

## RUN
if __name__ == "__main__":
    main()