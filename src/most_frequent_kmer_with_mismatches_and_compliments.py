__author__ = 'nikita_kartashov'

from algo_primitives.frequency_array import most_frequent_kmers_with_mismatches


if __name__ == '__main__':
    TEXT = 'GCAAGGTGACAAGCGTGCACGTGACCGTAAGCGTACAAGGTGGTGGTGGCGTGCGTACGTGGTGACGCACGCGCAAGGCCGTACGCGCGCCGTGTGGCGCGCCGTCGTGCCGTGCCGTCGTCGTAAGGCGCCGTAAGCGTGTGGCAAGCGTACGTGGTGGTGGTGACCGTCGTACGTGCGTCGTACACAAGCGTGTGGCGTGGTGACACACAAGGCAAGCGT'

    k = 9
    d = 2
    # print(' '.join(most_frequent_kmers(TEXT, k, d)))
    print(' '.join(most_frequent_kmers_with_mismatches(TEXT, k, d, with_complements=True)))
