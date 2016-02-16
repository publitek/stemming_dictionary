"""Expands the dictionary file performing the necessary modifications to make it more suitable for stemming"""
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
    # SWEAT != SWEATER
    'sweat': '',
    'sweater': 'S',
    # LANDSCAPING != LANDSCAPE
    'landscape': 'ZSRD',
    # HAMBURGER != HAMBURG
    'hamburger': 'S',
    'hamburg': '',
    # OFFICER != OFFICE
    'officer': 'S',
    'office': 'S',
}


class Expander:
    """Expands the dictionary file performing the necessary modifications to make it more suitable for stemming"""
    dictionary = {}

    def run(self):
        """Performs the expansion"""
        self.load_original()

        # Stem *men -> *man, etc.
        remove_words = []
        for word, params in self.dictionary.items():
            remove_words += self.process_word(word)

        # Remove words
        for word in remove_words:
            del self.dictionary[word]

        # Merge with adjustments
        self.dictionary.update(ADJUSTMENTS)

        # Remove entries without params
        self.dictionary = dict((word, params) for word, params in self.dictionary.items() if params)

        self.write_new_dict()

    def process_word(self, word):
        """
        Processes a given word.
        :param word: The word to process
        :returns: List of words to remove from the dictionary
        """
        remove_words = []
        for safe_end, (old_end, new_param) in NEW_STEMS.items():
            if word.endswith(safe_end):
                man_word = (word.rsplit(safe_end, 1)[0] + old_end)
                if man_word in self.dictionary:
                    self.dictionary[man_word] += new_param
                    remove_words.append(word)
        return remove_words

    def load_original(self):
        """Loads in the original dictionary, removing prefix and suffixes defined above"""
        with open('en_US.dic.orig') as f:
            for line in f:
                try:
                    # Split entries into words and params
                    word, params = line.strip().split('/')
                except ValueError:
                    word, params = line.strip(), ''

                new_words = []

                # Remove prefixes
                for key, prefix in PFX_TO_REMOVE.items():
                    if key in params:
                        params = params.replace(key, '')
                        new_words.append(prefix + word)

                # Remove suffixes
                for suffix in SFX_TO_REMOVE:
                    params = params.replace(suffix, '')

                # Only add words longer than 1 char
                if len(word) > 1:
                    self.dictionary[word] = params

                    # Add new words
                    for new_word in new_words:
                        if new_word in self.dictionary:
                            params = ''.join(set(self.dictionary[new_word] + params))
                        self.dictionary[new_word] = params

    def write_new_dict(self):
        """Writes the new dictionary to en_US.dic"""
        with open('en_US.dic', 'w') as f:
            words = sorted(self.dictionary.keys())
            f.write('%d\n' % (len(words)))
            for word in words:
                f.write('{}/{}\n'.format(word, self.dictionary[word]))


if __name__ == "__main__":
    Expander().run()
