# brute.bip39
Get valid bip39 seed from incomplete seed

Open the brute.py file and edit the `seed23words` variable with your 23 words.

Then, run `python brute.py`.

It will give you 180 possible valid BIP39 seeds.

If the size of your seed is not 24, change the number `24` from this line (from `brute.py`):

`for arridx in range(0,24):`
