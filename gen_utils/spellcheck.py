#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Spellcheck Script
"""

from spellchecker import SpellChecker  # pip install pyspellchecker
import sys

#### Params ####

show_only_words = False
multiple_recommendations = False
max_recommendations = 5  # Only matters if multiple_recommendations is True
only_show_words_with_recommendations = True

################


def instructions():
    print("\n\tSyntax: python spellcheck.py [input filename]")
    print("\tAll words in the file must be separated by newlines")
    print("\tParams must be modified directly from the file\n")


def spellcheck(input_file):

    # Read word set from input_file
    with open(input_file, "r") as file:
        word_list = file.read().split("\n")
    # print(content_list)

    spell = SpellChecker()

    # find those words that may be misspelled
    misspelled = spell.unknown(word_list)

    index = 0
    changes = []

    for word in misspelled:
        if word != "":

            corrected = ""
            s = str(index) + ". " + word

            if not show_only_words:
                corrected = spell.correction(word)
                # Fetch the best autocorrect
                s += " --> " + corrected
                # Fetch a list of other potential spell options (optional)
                if multiple_recommendations:
                    s += "; " + str(list(spell.candidates(word))
                                    [:max_recommendations])

            if not only_show_words_with_recommendations or word != corrected:
                changes.append(s)
                index += 1

    # Write results to file output_file
    with open(input_file.split(".")[0] + "_output" + ".txt", 'w') as writer:
        for c in changes:
            writer.write(c + "\n")


if len(sys.argv) < 2:
    instructions()
else:
    try:
        spellcheck(sys.argv[1])
    except:
        print("\n\tInvalid file!")
        instructions()
