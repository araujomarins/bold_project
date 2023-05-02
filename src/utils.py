from typing import List
import spacy

from .definition import IMPORTANT_KEYWORDS

def is_personal_name_or_city_name(string: str) -> bool:
    """Determines if the given string contains a named entity of type PERSON, GPE or LOC.

    Args:
        string: A string.

    Returns:
        A boolean indicating whether the input string contains a named entity of type PERSON, GPE or LOC.
    """
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(string)
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'GPE', 'LOC']:
            return True
    return False

def clean_list(string_list: str) -> List[str]:
    """Cleans a list of strings by splitting them at newline characters and appending important keywords.

    Args:
        string_list: A string containing a list of strings separated by newline characters.

    Returns:
        A list of strings containing the split strings from the input and important keywords.
    """
    keyowrds_list = []

    for l in string_list:
        keyowrds_list.extend(l.split("\n"))

    for kw in IMPORTANT_KEYWORDS:
        if kw not in keyowrds_list:
            keyowrds_list.append(kw)

    return keyowrds_list
