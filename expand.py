## PREFIXES TO REMOVE
PFX_TO_REMOVE = {
    'A': 're',
    'I': 'in',
    'U': 'un',
    'C': 'de',
    'E': 'dis',
    'F': 'con',
    'K': 'pro',
}

## SUFFIXES TO REMOVE
SFX_TO_REMOVE = [
    'M',
]

## UPDATE ORIGINAL WORDS WITH THESE CHANGES
ADJUSTMENTS = {
    'Olive': '',
    'Say': '',
    'aft': '',
    'after': '',
    'both': '',
    'broth': '',
    'ewe': 'S',
    'hove': '',
    'hunk': 'S',
    'int': '',
    'lee': 'S',
    'ling': '',
    'marine': 'S',
    'mariner': 'S',
    'moth': '',
    'muffle': 'SDG',
    'muffler': 'S',
    'neut': '',
    'staple': 'SDG',
    'stapler': 'S',
    'tattoo': 'SDG',
    'terry': 'S',
    'terrier': 'S',
}

## MAIN
def main():
    dictionary = {}
    ## OPEN ORIGINAL DICTIONARY
    with open('en_US.dic.orig2') as f:
        for line in f:
            try:
                ## SPLIT ENTIRES INTO WORDS AND PARAMS
                word, params = line.strip().split('/')
            except ValueError:
                pass
            else:
                ## NEW WORDS LIST
                new_words = []
                ## REMOVE PREFIXES
                for key, prefix in PFX_TO_REMOVE.items():
                    if key in params:
                        params = params.replace(key, '')
                        ## ADD NEW WORD TO 
                        new_words.append(prefix + word)
                ## REMOVE SUFFIXES
                for suffix in SFX_TO_REMOVE:
                    params = params.replace(suffix, '')
                ## ADD WORD TO DICTIONARY
                dictionary[word] = params
                ## ADD NEW WORDS TO DICTIONARY
                for new_word in new_words:
                    if new_word in dictionary:
                        params = ''.join(set(dictionary[new_word] + params))
                    dictionary[new_word] = params
    ## MERGE WITH ADJUSTMENTS
    dictionary.update(ADJUSTMENTS)
    ## REMOVE ENTRIES WITHOUT PARAMS
    dictionary = dict((word, params) for word, params in dictionary.items() if params)
    ## WRITE CHANGE TO NEW DICTIONARY
    with open('en_US.dic', 'w') as f:
        words = sorted(dictionary.keys())
        f.write('%d\n'%(len(words)))
        for word in words:
            f.write('%s/%s\n'%(word, dictionary[word]))

## RUN
if __name__ == "__main__":
    main()
