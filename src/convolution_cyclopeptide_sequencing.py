__author__ = 'nikita_kartashov'

from collections import Counter

from noisy_cyclopeptide_sequencing import noisy_cyclopeptides_with_spectrum, peptide_pretty, string_to_spectrum
from spectrum_convolution import spectrum_convolution
from utils.pyutils import top_by_snd_and_ignore, fst, filter_between


def convolution_cyclopeptides(spectrum, m, n):
    convolution = spectrum_convolution(spectrum)
    filtered_alphabet = list(filter_between(convolution, 57, 200))
    alphabet = top_by_snd_and_ignore(Counter(filtered_alphabet).most_common(), m, descending=True, with_ties=True)
    return noisy_cyclopeptides_with_spectrum(spectrum, n, alphabet)


if __name__ == '__main__':
    STRING = '0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322'
    M = 20
    N = 1000
    spectrum = string_to_spectrum(STRING)
    print(' '.join(map(peptide_pretty, convolution_cyclopeptides(spectrum, M, N))))
    # print(peptide_pretty(fst(convolution_cyclopeptides(spectrum, M, N))))


