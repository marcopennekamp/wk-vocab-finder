max_level = 4

def read_level(level):
    kanji_list = []
    with open('kanji/level' + str(level) + '.kanji') as f:
        kanji_list = f.readlines()
    # Strip all newlines, convert to unicode and put into set.
    return {kanji.strip('\n') for kanji in kanji_list}

# Read all levels.
kanji_sets = []
for level in range(0, max_level + 1):
    last_set = (kanji_sets[level - 1] if level > 0 else set())
    current_set = read_level(level)
    kanji_sets.append(last_set | current_set)

# Read vocabulary.
vocab_list = 0
with open('data/6k.vocab') as f:
    vocab_list = f.readlines()
    vocab_list = [vocab.strip('\n') for vocab in vocab_list]

def testVocab(vocab, kanji_set):
    for c in vocab:
        if c not in kanji_set:
            # print("Failed at: " + c)
            return False
    return True

# Generate list of all vocabulary for all levels.
cont_vocab_lists = []
for i in range(0, max_level + 1):
    cont_vocab_lists.append([])

for vocab in vocab_list:
    level = 0
    for kanji_set in kanji_sets:
        if testVocab(vocab, kanji_set):
            cont_vocab_lists[level].append(vocab)
            break
        level = level + 1

# Write the lists to files.
level = 0
for cont_vocab in cont_vocab_lists:
    with open('result/level' + str(level) + '.vocab', 'w+') as f:
        for word in cont_vocab:
            f.write(word + '\n')
    level = level + 1
