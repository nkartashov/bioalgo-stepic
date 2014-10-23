__author__ = 'nikita_kartashov'

from functools import reduce

from utils.bioutils import kmer_to_index, kmers_with_d_mismatches, index_reverse_compliment_lazy, index_to_kmer, \
    one_mismatches

def build_frequency_array(source, kmer_size):
    result = [0] * 4 ** kmer_size

    def folder(array, index):
        array[index] += 1
        return array

    return reduce(folder,
                  (kmer_to_index(source[i: i + kmer_size]) for i in range(len(source) - kmer_size + 1)),
                  result)


def most_frequent_kmers_with_mismatches(text, k, d, with_complements=False):
    frequency_array = [0] * 4 ** k
    for s in (kmers_with_d_mismatches(text[i: i + k], d) for i in range(len(text) - k + 1)):
        for i in map(kmer_to_index, s):
            frequency_array[i] += 1
    if with_complements:
        half_length = len(frequency_array) // 2
        frequency_array = [f + frequency_array[index_reverse_compliment_lazy(i, k)] for i, f in
                           enumerate(frequency_array[: half_length])]
    max_frequency = max(frequency_array)
    return map(lambda i: index_to_kmer(i, k),
               (i for i, f in enumerate(frequency_array) if f == max_frequency))


if __name__ == '__main__':
    print(build_frequency_array('AAGCAAAGGTGGG', 2))
    print(kmer_to_index('ATGCAA'))
    print(index_to_kmer(5437, 7))
    print(index_to_kmer(5437, 8))
    print('\n'.join(one_mismatches('ATGCAA')))
    print('\n'.join(kmers_with_d_mismatches('ATGCAACGTTTGACAAA', 3)))

