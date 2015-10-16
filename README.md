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

### Tests

The testing code has been redone with a txt input file in the following format.

`term` = Don't Stem (term doesn't stem)

`term1;term2` = Should Stemp (term1 stems to term2)

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
http://archive.services.openoffice.org/pub/mirror/OpenOffice.org/contrib/dictionaries/