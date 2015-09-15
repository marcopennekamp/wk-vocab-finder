import sys

# Arguments
path = sys.argv[1]

words = []
with open(path) as f:
    lines = f.readlines()
    length = len(lines)
    i = 0
    while i < length:
        words.append(lines[i].strip('\n'))
        i += 3 # Only extract every third word.

for word in words:
    print(word)
