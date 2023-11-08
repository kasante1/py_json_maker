#!/usr/bin/python3
import re


def tokenize_sentence(sentence: str):

    split_sentence = re.split(r'[.!?]', sentence, flags=re.IGNORECASE)

    for sentence in split_sentence:
        yield sentence