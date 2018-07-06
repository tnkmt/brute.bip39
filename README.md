# brute.bip39 : Get valid bip39 seeds from incomplete seed (find the valid seeds with brute force)

Open the `brute.py` file and edit the `seed23words` variable with your 23 words.

Then, run `python brute.py`.

It will give you 180 possible valid BIP39 seeds.

If the size of your seed is not 24, change the number `24` from this line (from `brute.py`):

`for arridx in range(0,24):`

The `mnemonic.py` file is copied from <a href="https://raw.githubusercontent.com/trezor/python-mnemonic/master/mnemonic/mnemonic.py">Trezor</a>.

. . .

Oops, I tried to invent the wheel. There is already advanced tool for this task: https://github.com/gurnec/btcrecover

