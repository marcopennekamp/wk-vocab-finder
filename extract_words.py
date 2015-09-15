import sys
import re

# Arguments
path = sys.argv[1]

words = []
with open(path) as f:
    text = f.read()
    groups_list = re.findall("([^\s]+)\s*\[([^\s^\]]*)\]", text)
    for groups in groups_list:
        word = groups[0]
        reading = groups[1]
        if word != reading: # Only extract words that contain Kanji.
            words.append(word)

for word in words:
    print(word)
