#
# Copyright (c) 2018 tnkmt
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


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

