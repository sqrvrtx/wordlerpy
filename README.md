# wordlerpy
Helper App for Daily Wordle Problem

## Features


Helps narrow down the list of possible solutions in Wordle.


## Usage

Use as follows:

For example if the solution is TACIT: If you get stuck and if you have the following fixed letters already, 'A' at position 2, 'I' at 4, and 'T' at 5, ie *A*IT

    python wordler.py -f '*A*IT'

or if you had 'A', 'I' and 'T' but you are unsure of the order:

    python wordler.py -v 'AIT'


