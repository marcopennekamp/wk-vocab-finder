from util import *

max_level = 60

kanji_sets = read_all_levels(max_level)

# Read vocabulary.
vocab_list = read_word_list('data/6k.vocab')

# Generate list of all vocabulary for all levels.
cont_vocab_lists = []
for i in range(0, max_level + 1):
    cont_vocab_lists.append([])

for vocab in vocab_list:
    level = get_word_level(vocab, kanji_sets)
    if level >= 0:
        cont_vocab_lists[level].append(vocab)

# Write the lists to files.
level = 0
for cont_vocab in cont_vocab_lists:
    with open('result/level' + str(level) + '.vocab', 'w+') as f:
        for word in cont_vocab:
            f.write(word + '\n')
    level = level + 1
