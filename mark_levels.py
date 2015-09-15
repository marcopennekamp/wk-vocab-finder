import sys
from util import *

# Arguments
file_name = sys.argv[1]

max_level = 60
kanji_sets = read_all_levels(max_level)
vocab_list = read_word_list('6k/' + file_name + '.vocab')

leveled_vocab_list = []
for vocab in vocab_list:
    # Also sets the level to -1 when the vocab can't be represented.
    leveled_vocab_list.append((vocab, get_word_level(vocab, kanji_sets)))

# Sort by level.
leveled_vocab_list = sorted(leveled_vocab_list, key = lambda vocab: vocab[1])

# Write the list to the file.
with open('leveled/' + file_name + '.txt', 'w+') as f:
    for vocab in leveled_vocab_list:
        f.write(
            vocab[0].ljust(10, '\u3000')
            + ' '
            + str(vocab[1]).rjust(2)
            + '\n'
        )
