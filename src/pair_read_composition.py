__author__ = 'nikita_kartashov'

from utils.pyutils import fst, snd


def pair_read_composition(string, k, d):
    return ((string[i: i + k], string[i + k + d: i + 2 * k + d]) for i in range(len(string) - 2 * k - d + 1))


def pretty_pair_read(reads):
    def mapper(read):
        return '({0}|{1})'.format(fst(read), snd(read))

    return ' '.join(map(mapper, sorted(reads)))


if __name__ == '__main__':
    STRING = 'TAATGCCATGGGATGTT'
    K = 3
    D = 2
    print(pretty_pair_read(pair_read_composition(STRING, K, D)))
