"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # create an empty dictionary
    word_count = {}

    # convert string into list of words
    words = phrase.split()

    # iterate over each word in list.
    for word in words:

        # adds word if it's not in dictionary, and starts value at 1
        if word not in word_count:
            word_count[word] = 1

        # if word is in dictionary, increments value by 1
        else:
            word_count[word] += 1

    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    # create a dictionary with melons as keys and prices as values
    melon_prices = {'watermelon' : 2.95,
                    'cantaloupe' : 2.50,
                    'musk' : 3.25,
                    'christmas' : 14.25
                    }
    
    # returns the value of the melon
    # if the melon does not exit, returns 'No price found'
    return melon_prices.get(melon_name.lower(), 'No price found')


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    # create an empty dictionary
    word_lengths = {}

    # sorts list alphabetically
    words.sort()

    # iterate over each word in list
    for word in words:

        # checks length of word.
        # if word length is not in dictionary, adds the word length as a key and
        # the word as a value.
        if len(word) not in word_lengths:
            word_lengths[len(word)] = [word]

        # if word length is in dictionary, adds the word as an additional value.
        else:
            word_lengths[len(word)] += [word]

    # returns sorted list of key/value pair items in the dictionary
    return sorted(word_lengths.items())

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    # create dictionary of English/Pirate translations
    english_to_pirate = {
                        'sir' : 'matey',
                        'hotel' : 'fleabag inn',
                        'student' : 'swabbie',
                        'man' : 'matey',
                        'professor' : 'foul blaggart',
                        'restaurant' : 'galley',
                        'your' : 'yer',
                        'excuse' : 'arr',
                        'students' : 'swabbies',
                        'are' : 'be',
                        'restroom' : 'head',
                        'my' : 'me',
                        'is' : 'be'
                        }

    # converts phrase into list of words
    phrase = phrase.split()

    # creates empty list for translated words
    translated_words = []

    # iterate over each word in phrase and checks if word in phrase is in dictionary.
    # if word is in dictionary, replace word with pirate-speak, and append to
    # translated word list.
    for word in phrase:
        if word not in english_to_pirate:
            translated_words.append(word)

        # if word is not in dictionary, appends word to translated word list.
        else:
            translated_words.append(english_to_pirate[word])

    # converts list to a string, and joins each item with a space.
    return ' '.join(translated_words)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # create a new list containing the first name from the list
    # removes the first name from the names list
    chain = [names.pop(0)]

    # create an empty dictionary
    names_by_letter = {}

    # iterate over each name in names
    for name in names:

        # checks if the first letter in the name is in the dictionary
        # if not, adds the letter in the dictionary with the name as the value
        if name[0] not in names_by_letter:
            names_by_letter[name[0]] = [name]

        # if the letter is in the dictionary, adds the name as an additonal value
        else:
            names_by_letter[name[0]] += [name]

    # checks if the last letter of the last name in the chain is in the dictionary
    # if the letter is in the dictionary, a new variable 'new_name' is created
    # to hold the first value of the letter in the dictionary
    if chain[-1][-1] in names_by_letter:
        new_name = (names_by_letter[chain[-1][-1]][0])

        # loops until the new name is not in the names list
        # adds the new name to the chain list
        # removes the name from the names list and the dictionary
        # removal ensures the name is not used again
        while new_name in names:
            chain.append(new_name)
            names.remove(new_name)
            del names_by_letter[new_name[0]][0]

            # checks if the last letter of the last name in the chain is in the
            # dictionary.
            # if it is, also checks if the letter still has values
            # if the above is true, 'new_name' is reassigned to the value of the
            # letter
            if chain[-1][-1] in names_by_letter and names_by_letter[chain[-1][-1]] != []:
                new_name = (names_by_letter[chain[-1][-1]][0])

    return chain

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
