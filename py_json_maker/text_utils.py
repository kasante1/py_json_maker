#!/usr/bin/python3
import re
from typing import Any, Generator
import string


def tokenize_sentence(sentence: str) -> Generator[str, Any, None]:
    """
    strip texts by delimiters [.?!]    
    """

    split_sentence = re.split(r'[.!?]', sentence, flags=re.IGNORECASE)

    for sentence in split_sentence:
        yield sentence



def sanitize_texts(text: str) -> str:
    """
    strip punctuation marks, symbols
    from texts.
    """
    sanitized_text = text.translate(str.maketrans(' ', ' ', string.punctuation))
    
    return sanitized_text


if __name__ == "__main__":
    sanitize_texts(text)