ISCED_DESCRIPTION = {
    'ISCED 0': "early childhood education",
    'ISCED 1': "primary education",
    'ISCED 2': "lower secondary education",
    'ISCED 3': "upper secondary education",
    'ISCED 4': "post-secondary education",
    'ISCED 5': "short-cycle tertiary education",
    'ISCED 6': "bachelor's",
    'ISCED 7': "master's",
    'ISCED 8': "doctorate",
}

IMPORTANT_KEYWORDS = {
    "scholarship",
    # "success",
}

BLACKLIST_KEYWORDS = [
    "school", 
    "college",
    "student",
    "students",
    "home",
    "society",
    "background",
    "family",
    "community",
    "love",
    "proud",
    "passion",
    "essay",
    "carrer"
]

QUERY_TEMPLATES = {

    "keyword": """
    Extract keywords from the text bellow

    Text:
    
    {}

    The answer must be splitted between comma and space.
    The answer must contains less than 11 words.
    The answer should not include any person's name.
    Include any word that is a profession or job.

    Example:

    Input text: "My favorite game in The Last of Us, even though I do not play any games anymore."

    Output: games, favorite
    """,

    "summary": """
    Please extract the following information from the given text and return as a dictionary:

    - Context: The reson to create the scholarship
    - Area: The area of study around the scholarships creation
    - Target: The description of the eligible person
    - Level: The education level of the scholarship

    Text: 

    {}

    The answer must be a dictionary, with no exceptions

    """
}