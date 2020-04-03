#!/usr/bin/env python3
from collections import defaultdict
import json

etym_f = open('etymwn-20130208/etymwn.tsv', 'r')

etymologies = defaultdict(list)
for line in etym_f:
    word1, rel, word2 = line.split("\t")
    if rel != "rel:etymology": continue
    etymologies[word1].append(word2)

def get_languages(w, s):
    lang, word = w.split(": ")
    s.add(lang)
    for w2 in etymologies[w]:
        get_languages(w2, s)

every_language = set()
result = {}
for lang_word in sorted(etymologies.keys()):
    lang, word = lang_word.split(": ")
    every_language.add(lang)
    if lang == "eng":
        etym_languages = set()
        get_languages(lang_word, etym_languages)
        result[word] = sorted(etym_languages)

with open('language_list.json', 'w') as f:
  json.dump(sorted(every_language), f)


with open('languages.json', 'w') as f:
    json.dump(result, f)
