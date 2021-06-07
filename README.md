# stemming_dictionary
## Hunspell Stemming Dictionary

### Status

[![Build Status](https://travis-ci.org/publitek/stemming_dictionary.svg?branch=master)](https://travis-ci.org/publitek/stemming_dictionary)

### Description

This project was created to make the Hunspell en_US spelling dictionaries
more appropriate for stemming. They were initaily designed for spelling
and not stemming so there are some obvious problems.

- corner -> corn
- unhappy -> happy
- butter -> butt

### Setup
`
virtualenv ~/.virtualenvs/stemming
source ~/.virtualenvs/stemming/bin/activate
pip install hunspell
`

### Tests

The testing code has been redone with a txt input file in the following format.

`term` = Don't Stem (term doesn't stem)
`term1;term2` = Should Stemp (term1 stems to term2)

### Running Tests Manually

Run `python expand.py` to update the en_US.dic file
Then run `hunspell -d en_US` to test it

### License

This dictionary is based on a subset of the original
English wordlist created by Kevin Atkinson for Pspell
and  Aspell and thus is covered by his original
LGPL license.

The affix file is a heavily modified
version of the original english.aff file which was
released as part of Geoff Kuenning's Ispell and as
such is covered by his BSD license.

### Original Dictionaries
https://github.com/LibreOffice/dictionaries/tree/master/en

### Hunspell documentation
https://github.com/hunspell/hunspell
https://grammalecte.net/_misc/hunspell4.pdf
https://spylls.readthedocs.io/en/latest/hunspell.html
https://sourceforge.net/projects/hunspell/files/Hunspell/Documentation/