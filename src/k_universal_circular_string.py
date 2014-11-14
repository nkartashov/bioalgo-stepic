__author__ = 'nikita_kartashov'

from utils.bioutils import all_possible_kmers
from utils.pyutils import drop_last_n
from string_reconstruction import string_reconstruction

def k_universal_circular_string(k):
    alphabet = ['0', '1']
    kmers = all_possible_kmers(k, alphabet)
    return drop_last_n(string_reconstruction(kmers, cyclic=True), k - 1)


if __name__ == '__main__':
    K = 4
    print(k_universal_circular_string(K))