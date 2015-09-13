import csv

# Read all vocabulary.
vocab_list = []
with open('data/core6k.csv') as core_file:
    reader = csv.DictReader(core_file)
    for row in reader:
        vocab_list.append(row['Vocab-expression'])

# Read WaniKani vocabulary.
wk_vocab = set()
with open('data/wk.vocab') as f:
    read_list = f.readlines()
    wk_vocab = {vocab.strip('\n') for vocab in read_list}

# Filter WaniKani vocabulary and print other vocabulary.
for vocab in vocab_list:
    if vocab not in wk_vocab:
        print(vocab)
