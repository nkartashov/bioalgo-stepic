__author__ = 'nikita_kartashov'

from functools import reduce
import operator

REVERSE_PROTEIN_POSSIBILITIES = {
    'F': 2, 'L': 6, 'I': 3, 'V': 4, 'M': 1,
    'A': 4, 'D': 2, 'E': 2, 'G': 4, 'T': 4,
    'N': 2, 'K': 2, 'S': 6, 'R': 6, 'Q': 2,
    'Stop': 3, 'W': 1, 'C': 2, 'H': 2, 'Y': 2,
    'P': 4}


def count_mrna_possibilites(string):
    return reduce(operator.mul, [REVERSE_PROTEIN_POSSIBILITIES[letter] for letter in string]) * \
           REVERSE_PROTEIN_POSSIBILITIES['Stop']

if __name__ == '__main__':
    PROTEIN = 'VKLFPWFNQY'
    print(count_mrna_possibilites(PROTEIN) / REVERSE_PROTEIN_POSSIBILITIES['Stop'])
