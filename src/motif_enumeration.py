__author__ = 'nikita_kartashov'

from copy import copy
from functools import reduce

from utils.bioutils import all_possible_kmers_from_text, kmers_with_d_mismatches, kmer_to_index, index_to_kmer


def kmer_presence_in_strings(dna_strings, k, d):
    false_list = [False] * len(dna_strings)
    kmer_presence = list(map(lambda x: copy(false_list), [None] * (4 ** k)))

    def inner(kmers, dna_tuple):
        dna_index, dna = dna_tuple
        for kmer in all_possible_kmers_from_text(dna, k):
            for mismatch_kmer in kmers_with_d_mismatches(kmer, d):
                kmers[kmer_to_index(mismatch_kmer)][dna_index] = True
        return kmers

    reduce(inner, enumerate(dna_strings), kmer_presence)
    return kmer_presence


def motif_enumeration(dna_strings, k, d):
    return (index_to_kmer(index, k) for index, value in
            enumerate(map(all, kmer_presence_in_strings(dna_strings, k, d))) if value)


if __name__ == '__main__':
    DNA_STRINGS = 'GGATCCCCAAATCGCATTTTTAGCG CAGAAACTACTATGCATACCATTTT GCTGGATTGTGGGCAGACATTCGTC CTGGCCACTCGGATCATCCCATTAT ATGAGTTTTGCCGCGATTTTGCAGA GACCAGCTAGAACCCATTGTTACAA'.split()
    K = 5
    D = 1
    print(' '.join(motif_enumeration(DNA_STRINGS, K, D)))
