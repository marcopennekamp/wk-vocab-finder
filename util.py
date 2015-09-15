def read_word_list(path):
    word_list = []
    with open(path) as f:
        word_list = f.readlines()
    return [word.strip('\n') for word in word_list] # Strip all newlines.

def read_level(level):
    lst = read_word_list('kanji/level' + str(level) + '.kanji')
    return set(lst)

def read_all_levels(max_level):
    kanji_sets = []
    for level in range(0, max_level + 1):
        last_set = (kanji_sets[level - 1] if level > 0 else set())
        current_set = read_level(level)
        kanji_sets.append(last_set | current_set)
    return kanji_sets

def is_word_representable(word, kanji_set):
    for c in word:
        if c not in kanji_set:
            return False
    return True

# Returns -1 when the word can't be represented with the current kanji set.
def get_word_level(word, kanji_sets):
    level = 0
    for kanji_set in kanji_sets:
        if is_word_representable(word, kanji_set):
            return level
        level = level + 1
    return -1
