#!/usr/bin/python

import gzip
import re
import sys
from collections import defaultdict

def read_dict_file(filename):
    full_form_lexicon = defaultdict(list)
    for line in gzip.open(filename, 'r'):
        form, lemma, case, num, gender = line.rstrip().split('\t')
        full_form_lexicon[form].append(' '.join([lemma, case, num, gender]))
    return full_form_lexicon

full_form_lexicon = read_dict_file(sys.argv[1])
for line in sys.stdin:
    for token in re.split('\s+', line.rstrip()):
        print(token)
        if token in full_form_lexicon:
            print("  %s" % '\n  '.join(full_form_lexicon[token]))
        else:
            print("  Unknown token.")
