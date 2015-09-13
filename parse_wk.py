from html.parser import HTMLParser

class WkParser(HTMLParser):
    def __init__(self):
        self.inWord = False
        self.words = []
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            isVocab = False
            for attr in attrs:
                if attr[0] == 'lang':
                    isVocab = attr[1] == 'ja'
            if isVocab:
                self.inWord = True

    def handle_endtag(self, tag):
        self.inWord = False

    def handle_data(self, data):
        if self.inWord:
            self.words.append(data)

parser = WkParser()
with open('data/wk.html') as f:
    parser.feed(f.read())

for word in parser.words:
    print(word)
