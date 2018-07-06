import mnemonic
import sys

radix = 2048
with open('wordlist/english.txt', 'r') as f:
    wordlist = [w.strip().decode('utf8') if sys.version < '3' else w.strip() for w in f.readlines()]
if len(wordlist) != radix:
    raise ConfigurationError('Wordlist should contain %d words, but it contains %d words.' % (radix, len(wordlist)))

seed23words = "list boy acquire hand trade decline figure airport upset region galaxy decorate rain federal name badge prosper poem stage rebel promote hood peanut"

arr23 = seed23words.split(" ")

m = mnemonic.Mnemonic('english')

for arridx in range(0,24):
    for word in wordlist:
        arr23.insert(arridx,word)
        tested=" ".join(arr23)
        del arr23[arridx]
        if m.check(tested):
            print tested
