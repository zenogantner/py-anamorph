#!/usr/bin/python3

import sys
import xml.sax

INTERESTING_ATTRIBUTES = ['kas', 'num', 'gen']

class MorphyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.counter = 0
        self.current_form = None
        self.current_characters = None
        self.current_attributes = {}

    def startElement(self, name, attrs):
        if name == "lemma":
            self.current_attributes = attrs.copy()

    def endElement(self, name):
        if name == 'form':
            self.current_form = self.current_characters
        if name == 'lemma' and self.current_attributes['wkl'] == 'SUB':
            attribs = list(map(lambda k: self.current_attributes[k], INTERESTING_ATTRIBUTES))
            print('\t'.join([self.current_form, self.current_characters] + attribs))
            self.counter += 1
            if self.counter % 100000 == 0:
                sys.stderr.write('%s\n' % self.counter)

    def characters(self, content):
        self.current_characters = content


parser = xml.sax.make_parser()
parser.setContentHandler(MorphyContentHandler())
lexicon_filename = sys.argv[1]
parser.parse(open(lexicon_filename))
