# PREFIXES TO REMOVE
PFX_TO_REMOVE = {
    'A': 're',
    'I': 'in',
    'U': 'un',
    'C': 'de',
    'E': 'dis',
    'F': 'con',
    'K': 'pro',
}

# SUFFIXES TO REMOVE
SFX_TO_REMOVE = [
    'M',
]

# NEW STEMS
NEW_STEMS = {
    'people': ('person', 'Q'),
    'teeth': ('tooth', 'Q'),
    'geese': ('goose', 'Q'),
    'men': ('man', 'O'),
}

# UPDATE ORIGINAL WORDS WITH THESE CHANGES
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
    'mother': 'RDYZGS',
    'muffle': 'SDG',
    'muffler': 'S',
    'neut': '',
    'staple': 'SDG',
    'stapler': 'S',
    'tattoo': 'SDG',
    'terry': 'S',
    'terrier': 'S',
    'tee': 'DRS',
    'too': '',
    # ADDED CONMEN/GARBAGEMEN/GROUNDSMEN
    'conman': 'O',
    'garbageman': 'O',
    'groundsman': 'O',
    # BUTTER -> BUTT
    'butt': 'GDS',
    'butter': 'GDS',
    # CORNER -> CORN
    'corn': 'GDS',
    'corner': 'GDS',
    # EASTER -> EAST
    'east': 'GS',
    # TELEMARKET
    'telemarket': 'RGZ',
    'telemarketer': '',
    'telemarketing': '',
    # BEER/BEING -> BEE
    'beer': 'S',
    'bee': 'S',
    # CRATER -> CRATE
    'crate': 'DSGZ',
    # COUPLE/COUPLES
    'couples': '',
    'couple': 'S',
    # CHILD/CHILDREN
    'children': '',
    'child': 'GDSY',
    # SHOWER -> SHOW
    'show': 'GDJS',
    'shower': 'GDS',
    # TRAINING != TRAIN
    'train': 'S',
    # FISH ~!= FISHING
    'fish': 'ZSRD',
    'fishing': 'S',
    # PIG != PIGMENT
    'pig': 'S',
    # BADGER != BADGE
    'badge': 'DSG',
    'badger': 'DSG',
    # HAMBURG != HAMBURGER
    'hamburg': 'S',
    'hamburger': 'S',
    # WEATHER != WEATHERED
    'weather': 'RYJGS',
    # PANTS != PANT 
    'pant': 'DG',
    # DRESS != DRESSING != DRESSED
    'dress': 'S',
    # ACCOUNTING != ACCOUNT
    'account': 'BDS',
    # BEARING != BEAR
    'bear': 'ZBRS',
    'bearing': 'S',
    # BOND != BONDING
    'bond': 'RSZ',
    'bonding': 'S',
    # BOX != BOXING
    'box': 'DRSZ',
    'boxing': 'S',
    # DATE != DATING
    'date': 'RSZV',
    'dating': 'S',
    # DRAFT != DRAFTING
    'draft': 'DS',
    # FALL != FALLING
    'fall': 'SZRN',
    'falling': 'S',
    # ICE != ICING
    'ice': 'DS',
}

# MAIN
def main():
    dictionary = {}
    # OPEN ORIGINAL DICTIONARY
    with open('en_US.dic.orig') as f:
        for line in f:
            try:
                # SPLIT ENTIRES INTO WORDS AND PARAMS
                word, params = line.strip().split('/')
            except ValueError:
                word, params = line.strip(), ''
            # NEW WORDS LIST
            new_words = []
            # REMOVE PREFIXES
            for key, prefix in PFX_TO_REMOVE.items():
                if key in params:
                    params = params.replace(key, '')
                    # ADD NEW WORD TO 
                    new_words.append(prefix + word)
            # REMOVE SUFFIXES
            for suffix in SFX_TO_REMOVE:
                params = params.replace(suffix, '')
            # ADD WORD TO DICTIONARY
            dictionary[word] = params
            # ADD NEW WORDS TO DICTIONARY
            for new_word in new_words:
                if new_word in dictionary:
                    params = ''.join(set(dictionary[new_word] + params))
                dictionary[new_word] = params
    # REMOVE WORDS
    remove_words = []
    # STEM *MEN -> *MAN
    for word, params in dictionary.items():
        for safe_end, (old_end, new_param) in NEW_STEMS.items():
            if word.endswith(safe_end):
                man_word = (word.rsplit(safe_end, 1)[0] + old_end)
                if man_word in dictionary:
                    dictionary[man_word] += new_param
                    remove_words.append(word)
    # REMOVE WORDS
    for word in remove_words:
        del dictionary[word]
    # MERGE WITH ADJUSTMENTS
    dictionary.update(ADJUSTMENTS)
    # REMOVE ENTRIES WITHOUT PARAMS
    dictionary = dict((word, params) for word, params in dictionary.items() if params)
    # WRITE CHANGE TO NEW DICTIONARY
    with open('en_US.dic', 'w') as f:
        words = sorted(dictionary.keys())
        f.write('%d\n'%(len(words)))
        for word in words:
            f.write('%s/%s\n'%(word, dictionary[word]))

# RUN
if __name__ == "__main__":
    main()
