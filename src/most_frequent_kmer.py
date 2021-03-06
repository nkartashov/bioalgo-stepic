__author__ = 'nikita_kartashov'

from utils.pyutils import sliding, sort_by_snd, top_by_snd_and_ignore, fst
from pattern_count import pattern_count


def all_kmers(text, k):
    return set(sliding(text, k))


def pattern_frequencies(text, patterns):
    return [(pattern, pattern_count(text, pattern)) for pattern in patterns]


def most_frequent_kmers(text, k):
    kmers = all_kmers(text, k)
    freqs = pattern_frequencies(text, kmers)
    return top_by_snd_and_ignore(freqs)


if __name__ == '__main__':
    TEXT = 'CATGAGGGATGCAAGGGCCTACGTCATGAGGCATGAGGCTGTAACGTTGTGACGTCATGAGGCATGAGGTGTGACGTGGCCTACGTCATGAGGCATGAGGTGTGACGTCTGTAACGTTGTGACGTGGCCTACGTCTGTAACGTTGTGACGTCATGAGGGGCCTACGTTGTGACGTGATGCAAGGGCCTACGTGGCCTACGTCTGTAACGTTGTGACGTTGTGACGTTGTGACGTTGTGACGTGATGCAAGCATGAGGGGCCTACGTCTGTAACGTCATGAGGCATGAGGGGCCTACGTTGTGACGTGGCCTACGTTGTGACGTTGTGACGTCATGAGGCTGTAACGTGGCCTACGTCTGTAACGTTGTGACGTGGCCTACGTTGTGACGTGGCCTACGTTGTGACGTTGTGACGTCTGTAACGTCTGTAACGTGATGCAAGTGTGACGTGATGCAAGTGTGACGTCTGTAACGTGGCCTACGTGGCCTACGTCATGAGGGGCCTACGTCATGAGGCATGAGGTGTGACGTCATGAGGCTGTAACGTTGTGACGTGATGCAAGCATGAGGCTGTAACGTGATGCAAGTGTGACGTCTGTAACGTGGCCTACGTGGCCTACGTCTGTAACGTCTGTAACGTCATGAGGCATGAGGGGCCTACGTTGTGACGTCATGAGGCATGAGGCTGTAACGTGGCCTACGTTGTGACGTCTGTAACGTCTGTAACGTCTGTAACGTCTGTAACGTTGTGACGTGGCCTACGTCTGTAACGTCATGAGGGATGCAAGCTGTAACGT'
    k = 13

    print(' '.join(most_frequent_kmers(TEXT, k)))
    # print(len(most_frequent_kmers(TEXT, k)))


