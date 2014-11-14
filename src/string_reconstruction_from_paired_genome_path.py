__author__ = 'nikita_kartashov'

from utils.pyutils import fst, snd, head
from functools import reduce


def glue_together(left, right, left_start):
    right_overlap_start = len(left) - left_start

    def zipper(left_nucleotide, right_nucleotide):
        if left_nucleotide == ' ':
            return right_nucleotide
        if right_nucleotide == ' ':
            return left_nucleotide
        return left_nucleotide

    return '{0}{1}{2}'.format(left[:left_start],
                              ''.join(zipper(l, r) for l, r in zip(left[left_start:], right[:right_overlap_start])),
                              right[right_overlap_start:])


def space_paired_read(read, d):
    return fst(read) + ' ' * d + snd(read)


def string_reconstruction_from_paired_genome_path(path, d, k):
    def folder(acc, read_tuple):
        start, read = read_tuple
        return glue_together(acc, read, start)

    return reduce(folder, enumerate(map(lambda x: space_paired_read(x, d), path)), ' ' * (2 * k + d))


def parse_pairs(string):
    return (pair.strip('()').split('|') for pair in string.split('\n'))


if __name__ == '__main__':
    D = 1
    K = 2
    pairs = (pair.strip('()').split('|') for pair in
             '(AG|AG)->(GC|GC)->(CA|CT)->(AG|TG)->(GC|GC)->(CT|CT)->(TG|TG)->(GC|GC)->(CT|CA)'.split('->'))
    print(string_reconstruction_from_paired_genome_path(pairs, D, K))