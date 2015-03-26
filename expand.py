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

## BASE WORDS (remove all prefix / suffix rules, except those listed)
BASE_WORDS = {
    'Olive': '',
    'Say': '',
    'aft': '',
    'both': '',
    'broth': '',
    'ewe': 'S',
    'hove': '',
    'hunk': 'S',
    'int': '',
    'lee': 'S',
    'ling': '',
    'marine': 'S',
    'moth': '',
    'muffle': 'SDG',
    'neut': '',
    'staple': 'SDG',
    'tattoo': 'SDG',
    'terry': 'S'
}

# Add these words to the dictionary
ADD_WORDS = [
    'after/',
    'mariner/S',
    'muffler/S',
    'stapler/S',
    'terrier/S'
]

## MAIN
def main():
    dic = OrderedDict()
    with open('en_US.dic.orig') as f:
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
                if word in BASE_WORDS:
                    params = BASE_WORDS[word]
                if params:
                    dic[word] = params
                    for w in words:
                        dic[w] = params
    for add_word in ADD_WORDS:
        word, params = add_word.split('/')
        dic[word] = params
    with open('en_US.dic', 'w') as f:
        words = sorted(dic.keys())
        f.write('%d\n'%(len(words)))
        for word in words:
            f.write('%s/%s\n'%(word, dic[word]))

## RUN
if __name__ == "__main__":
    main()
