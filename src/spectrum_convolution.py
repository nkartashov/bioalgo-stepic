__author__ = 'nikita_kartashov'

from cyclopeptide_sequencing import string_to_spectrum
from functools import reduce
from operator import add


def spectrum_convolution(spectrum):
    spectrum = list(sorted(spectrum))

    def inner(i):
        return list(filter(lambda x: x > 0, (spectrum[i] - mass for mass in spectrum[:i])))

    return list(reduce(add, map(inner, range(len(spectrum)))))


if __name__ == '__main__':
    STRING = '184 614 1000 283 244 517 701 724 979 370 520 1131 257 1004 258 871 113 260 561 719 1005 984 805 795 1002 0 498 1149 832 873 389 1165 892 71 543 129 131 950 570 595 934 887 97 756 262 635 742 1191 667 186 1131 441 391 299 674 386 866 853 1262 764 1133 1018 627 1134 129 745 588 312 506 199 409 963 375 692 1115 328 457 821 538 876 396 1076 430 131 278 1078 467 648 128 1133 1063 147'
    spectrum = string_to_spectrum(STRING)
    print(' '.join(map(str, spectrum_convolution(spectrum))))
