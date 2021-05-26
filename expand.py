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
    # SHOW !+ SHOWING
    'show': 'DS',
    'showing': 'S',
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
    # 'pant': 'DG',
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
    'landscape': 'ZSR',
    # LANDSCPED != LANDSCAPE
    'landscaped': '',
    # LANDING -> LANDINGS
    'landing': 'S',
    # LANDSCAPING -> LANDSCAPINGS
    'landscaping': 'S',
    # LANDED != LAND
    'land': 'SRZ',
    # HAMBURGER != HAMBURG
    'hamburger': 'S',
    'hamburg': '',
    # OFFICER != OFFICE
    'officer': 'S',
    'office': 'S',
    # BUSINESS != BUSY
    'busy': 'DSRTG',
    # EARLY != EARLIES
    'early': 'PRT',
    # EAR != EARING, EARLY, EARTH
    'ear': 'SMD',
    # MOP != MOPED
    'mop': 'SMGJDRZ',
    'map': 'SMGJDRZ',
    'mope': 'SGZDR',
    'moper': '',
    'mopper': '',
    'mapper': '',
    'mopping': '',
    'mapping': '',
    # ONE != ONIONS
    'one': 'PS',
    'onion': 'SGD',

    # NEW
    # ACTIVATE
    'activate': 'DGNSX3',
    # ADAPTER != ADAPT
    'adapter': 'S35',
    'adapt': 'BDGSV',
    # ADD -> ADDING
    'add': 'BDGJRSZ',
    # ADMIRAL
    'admiral': 'S2',
    # ADORABLE != ADORE
    'adore': 'DSRGZB',
    'adorable': 'PY',
    # ALTERNATIVE != ALTERNATE
    'alternative': 'SY',
    'alternate': 'SDGNYX',
    # ARRANGEMENT != ARRANGE
    'arrangement': 'S',
    'arrange': 'ZDSRG',
    # AUTHORIZE -> AUTHORIZATION AUTHORIZER
    'authorize': 'GDSRZN',
    # BATHING != BATH
    'bath': 'DSRZ',
    'bathing': 'S',
    # BREAKING
    'breaking': 'S',
    'break': 'SZRB',
    # BUILDING != BUILD
    'build': 'S',
    'building': 'S',
    # BUSINESSES != BUSINESS
    'business': '',
    'businesses': '',
    # CAPITALIZE
    'capitalize': 'GN',
    # CAPITATE
    'capitate': 'SDGN',
    # CENT != CENTER
    'cent': 'S',
    'center': 'S',
    # CLOSED != CLOSE
    'close': 'SRG',
    'closed': '',
    # COLLECTIVE
    'collective': 'SY2',
    # COMBINATIONS != COMBINATION
    'combination': '',
    'combinations': '',
    # COLOR
    'color': 'SRDGZJ8',
    # COMPACTED != COMPACT
    'compact': 'TZGSPRY',
    'compacted': '',
    # CONCENTRIC
    'concentric': 'S',
    # COOK != COOKED or COOKING
    'cook': 'ZRS',
    'cooking': '',
    'cooked': '',
    # COOPERATE
    'cooperate': 'VNGXSD3',
    # CUSTOM != CUSTOMER
    'customer': 'S',
    'custom': '',
    'customs': '',
    # CUSTOMIZE
    'customize': 'ZGBSRDN',
    # DECORATE != DECORATED or DECORATING or DECORATION or DECORATIVE
    'decorate': 'S',
    'decorated': '',
    'decorating': 'S',
    'decoration': 'S',
    'decorative': '',
    # DEPENDABLE != DEPEND
    'depend': 'GDS',
    'dependable': '2',
    # DEPENDANT
    'dependant': 'S',
    # DESERTED != DESERT
    'desert': 'ZGRS',
    'deserted': '',
    # DESIGNER != DESIGN
    'design': 'DSG',
    'designer': 'S',
    # DISTILLER != DISTILL
    'distiller': 'S',
    'distill': 'GSD',
    # EARTH -> EARTHLY
    'earth': 'DNGY',
    # ECONOMIZE
    'economize': 'GZSRDN',
    # EFFECTIVE != EFFECT
    'effect': 'SDG',
    'effective': 'PY',
    # ELECTRICITY
    'electricity': 'S',
    # EXECUTIVE != EXECUTE
    'execute': 'NGZBXDRS',
    'executive': 'SY',
    # EXHAUSTED != EXHAUST
    'exhaust': '',
    'exhausted': '',
    # FARMING != FARM
    'farming': 'S',
    'farm': 'RDZS',
    # FAVORABLE -> FAVORABLY
    'favorable': 'PSY',
    # FEDERATE != FEDERATION
    'federation': 'S',
    'federate': 'SDVG',
    # FLAVOR != FLAVORING
    'flavoring': 'S',
    'flavor': 'SDRZ',
    # FLYING != FLY
    'fly': 'BDRSTZ',
    'flying': '',
    # FORMATION != FORMATE
    'formate': 'DGS',
    'formation': 'S',
    # GENERATE != GENERATION
    'generate': 'VGSD',
    'generation': 'S',
    # GINGERLY != GINGER
    'ginger': 'DGS',
    'gingerly': '',
    # GLASS != GLASSES
    'glass': 'GD',
    'glasses': '',
    # GROOM ! GROOMING or GROOMED
    'groom': 'ZSR',
    'grooming': 'S',
    # HARDCORAL
    'hardcoral': 'S',
    # HOSPITABLE
    'hospitable': 'P',
    # HUMANE
    'humane': 'PY',
    # INFLATE != INFLATABLE or INFLATION
    'inflate': 'GDRS',
    'inflatable': 'S',
    'inflation': 'S',
    # INITIATE
    'initiate': 'GNS3',
    # INTEGRATE
    'integrate': 'DGNS3',
    # INTEREST != INTERESTING or INTERESTED
    'interest': 'S',
    'interesting': 'YPS',
    'interested': '',
    # INTERMENT != INTERN
    'intern': 'DGS',
    'internment': 'S',
    # INTERNALIZE
    'internalize': 'DGJS',
    # INTERNATIONAL
    'international': 'SY1',
    # IRONIC
    'ironic': '67',
    'ironical': 'P',
    # LIBERAL
    'liberal': 'YSP1',
    # LIBERATE
    'liberate': 'GDS35',
    'liberator': '',
    # LIBERATION != LIBERATE
    'liberation': 'S',
    # LEAVE != LEAVES
    'leave': 'RDZ',
    # LEAVING != LEAVE
    'leaving': 'S',
    # LIQUIDATE
    'liquidate': 'DGNSX35',
    'liquidator': '',
    # LONGING != LONG
    'long': 'DPRSTY',
    'longing': 'SY',
    # MAKING != MAKE
    'make': 'S',
    'making': 'S',
    # MATCHING != MATCH
    'match': 'BRSDZ',
    'matching': 'S',
    # MARBLE != MARBLES
    'marble': 'JRDG',
    'marbles': '',
    # MEDICATE != MEDICATION
    'medication': 'S',
    'medicate': 'DXGVS',
    # MODERNIZE
    'modernize': 'SRDGZN',
    # NEW != NEWS
    'new': 'PTGDRY',
    'news': '',
    # OBJECTIVE != OBJECT
    'object': 'SGD',
    'objective': 'S',
    # OPERATION!= OPERATE
    'operation': 'S6',
    'operate': 'GDS',
    # OPERATIVE
    'operative': 'S',
    # ORGANIZER != ORGANIZE
    'organizer': 'S',
    'organize': 'GDS',
    # ORIENTAL
    'oriental': 'SY1',
    # ORENTATE
    'orientate': 'SDXGN3',
    'orientation': '',
    # ORIENTEER
    'orienteer': 'GJ',
    # ORIGINAL
    'original': 'SY2',
    # ORIGINATE
    'originate': 'VGNXSD3',
    # PAINTERLY != PAINTER
    'painter': '',
    'painterly': 'P',
    # PAINTING != PAINT
    'paint': 'DRZS',
    'painting': 'S',
    # PANT != PANTING
    'pant': 'D',
    'panting': 'S',
    # PARK != PARKING(s) or PARKED or PARKER
    'park': 'S',
    'parking': 'S',
    'parked': '',
    # PEACEFUL
    'peaceful': 'PY',
    # PERFORM != PERFORMER
    'performer': 'S',
    'perform': 'SDGB',
    # PERSONALS != PERSONAL
    'personal': 'Y8',
    'personals': '',
    # PHYSICS != PHYSIC
    'physic': '',
    'physicS': '',
    # POINT != POINTER
    'point': 'DGS',
    'pointer': 'S',
    # POLITIC
    'politic': 'S67',
    # POSITIVE
    'positive': 'RSPYT2',
    # PRESENTABLE != PRESENT
    'present': 'SLDYZP',
    'presentable': 'P2',
    'presenter': 'S',
    # PRESERVER != PRESERVE
    'preserver': 'S',
    'preserve': 'DSBG',
    # PRODUCTIVE != PRODUCT
    'product': 'S',
    'productive': 'PY24',
    # PUBLICATE
    'publicate': 'SDNX',
    'publication': '',
    # PUZZLED != PUZZLE
    'puzzle': 'RSZL',
    'puzzled': '',
    'puzzling': '',
    # RAILING != RAIL
    'rail': 'DS',
    'railing': 'S',
    # RATIONAL
    'rational': 'YNPS128',
    'rationalize': '',
    # RECORD != RECORDING or RECORDER
    'record': 'S',
    'recorder': 'S',
    'recording': 'S',
    # REFER
    'refer': 'BR6',
    # RESPONSIBLE
    'responsible': 'PY24',
    'responsibility': '',
    # ROLLED != ROLL
    'roll': 'S',
    'rolled': '',
    'rolling': 'S',
    # SACRED
    'sacred': 'PYS',
    # SEASON != SEASONING(s)
    'season': 'RDYBZS',
    'seasoning': 'S',
    # SECRETED != SECRET
    'secret': 'TVRYS',
    'secrete': 'XNSDG',
    # SELECTIVE != SELECT
    'select': 'PDSGB',
    'selective': 'Y2',
    # SETTING != SETT
    'sett': '',
    # SEVERE
    'severe': 'PSY24',
    'severity': '',
    # SETTINGS != SETT
    'setting': 'S',
    # SHORT != SHORTS
    'short': 'GTXYRDNP',
    'shorts': '',
    # SHORTEN != SHORTENING (noun)
    'shorten': 'RD',
    # SINK != SINKING
    'sink': 'ZSRB',
    'sinking': 'S',
    # STOCKING != STOCK
    'stock': 'DS',
    'stocking': 'S',
    # TENDER != TEND
    'tend': 'SDG',
    'tender': 'DGS',
    # TENDERIZE
    'tenderize': 'NDRG',
    # TIRE !+ TIRING or TIRED
    'tire': 'S',
    'tired': 'Q',
    # TRANSFORMER != TRANSFORM
    'transform': 'DBSG',
    'transformer': 'S',
    # TRANSITION
    'transition': 'DGS6',
    # TRANSITIVE != TRANSIT
    'transit': 'SGD',
    'transitive': 'PY',
    # USED != USE or US
    'us': 'RSBZ',
    'use': 'S',
    'used': '',
    'using': '',
    # VEGETATION != VEGETATE
    'vegetation': 'S',
    'vegetate': 'DSGV',
    # WATCHING != WATCH
    'watch': 'RSDZB',
    'watching': '',
    # WAVED != WAVE
    'wave': 'ZRS',
    'waved': '',
    # WAVING != WAVE
    'waving': 'S',
    # WINDING != WIND
    'wind': 'SRZ',
    'winding': 'S',
    # WINTERIZE
    'winterize': 'DGNS',
    # WOODS != WOOD
    'wood': 'NDG',
    'woods': '',


    'loafer': 'S',


    # Adding irregular plurals -f to -ves
    # 'calf': 'W',
    'elf': 'W',
    # 'half': 'PW',
    'hoof': 'DRSGW',
    'knife': 'DSGW',
    'leaf': 'GSDW',
    # 'life': 'ZRW',
        # loaf != loafer | loafing | loafed
    'loaf': 'SW',
    'scarf': 'SDGW',
    # 'shelf': 'DGSW',
    # 'thief': 'W',   # add thieving?
    'wharf': 'SGDW',
    'wife': 'DSYGW',
    'wolf': 'RDGSW',

    # more irregular plurals
    'mouse': 'SRDGZQ',
    'cactus': 'SQ',
    'fungus': 'SQ',
    'octopus': 'SQ',
    'syllabus': 'SQ',
    'foot': 'SRDGZJQ',
    'quiz': 'Q',
    'potato': 'Q',
    'tomato': 'Q',

    # irregular verbs
    'sleep': 'RGZSQ',
    'swim': 'SQ',
    'teach': 'GSQ',
    'throw': 'SZGRQ',
    'understand': 'RGSJBQ',
    'write': 'SBRJGQ',

    # CONCENTRATE != CONCENTRATION

    # # NUMBERS
    # '1': '0',
    # '2': '0',
    # '3': '0',
    # '4': '0',
    # '5': '0',
    # '6': '0',
    # '7': '0',
    # '8': '0',
    # '9': '0',




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
