__author__ = 'nikita_kartashov'

from itertools import product
from functools import reduce

from utils.pyutils import flatten_to_set

GC = 'G', 'C'
AT = 'A', 'T'
NUCLEOTIDES_IN_CODON = 3


def map_nucleotide_to_two_bits(nucleotide):
    if nucleotide == 'A':
        return 0
    if nucleotide == 'C':
        return 1
    if nucleotide == 'G':
        return 2
    if nucleotide == 'T':
        return 3


NUCLEOTIDES = ['A', 'C', 'G', 'T']


def index_reverse_compliment_lazy(index, k):
    return kmer_to_index(reverse_compliment(index_to_kmer(index, k)))


def two_bits_to_nucleotide(two_bits):
    return NUCLEOTIDES[two_bits]


def index_to_kmer(index, k):
    length = k * 2
    return ''.join(map(two_bits_to_nucleotide, reversed(
        [((index >> i) & 3) for i in range(0, length, 2)])))


def kmer_to_index(kmer):
    def collapse(acc, x):
        return (acc << 2) ^ x

    return reduce(collapse, map(map_nucleotide_to_two_bits, kmer))


def find(letter, t):
    return t[0] if t[1] == letter else t[1]


def letter_compliment(letter):
    return find(letter, GC) if letter == 'G' or letter == 'C' else find(letter, AT)


def reverse_compliment(dna):
    return ''.join(list(map(letter_compliment, reversed(dna))))


def dna_to_rna(dna):
    return map(lambda x: 'U' if x == 'T' else x, dna)


def hamming_distance(text1, text2):
    def mapper(x):
        return 0 if x[0] == x[1] else 1

    return sum(map(mapper, zip(text1, text2)))


def all_possible_kmers(length):
    alphabet = ['A', 'C', 'T', 'G']
    return (''.join(t) for t in product(alphabet, repeat=length))


def all_possible_kmers_from_text(text, k):
    if len(text) < k:
        return []
    return (text[i: i + k] for i in range(len(text) - k + 1))


def one_mismatches(kmer):
    return flatten_to_set([[kmer[:i] + ch + kmer[i + 1:] for ch in NUCLEOTIDES]
                           for i in range(len(kmer))])


def kmers_with_d_mismatches(kmer, d):
    result = {kmer}
    for i in range(d):
        result = flatten_to_set(map(one_mismatches, result))
    return result


def forward_reading_frames(dna):
    return [dna, dna[1:], dna[2:]]


def reverse_reading_frames(dna):
    reversed_complimentary_chain = reverse_compliment(dna)
    return [reversed_complimentary_chain,
            reversed_complimentary_chain[1:],
            reversed_complimentary_chain[2:]]


def all_possible_reading_frames(dna):
    return forward_reading_frames(dna) + reverse_reading_frames(dna)
