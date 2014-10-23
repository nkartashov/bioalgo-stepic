__author__ = 'nikita_kartashov'

from noisy_cyclopeptide_sequencing import noisy_cyclopeptides_with_spectrum, string_to_spectrum, peptide_pretty

if __name__ == '__main__':
    MASS_STRING = '0 97 99 114 128 147 147 163 186 227 241 242 244 260 261 262 283 291 333 340 357 385 389 390 390 405 430 430 447 485 487 503 504 518 543 544 552 575 577 584 632 650 651 671 672 690 691 738 745 747 770 778 779 804 818 819 820 835 837 875 892 917 932 932 933 934 965 982 989 1030 1039 1060  1061 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1225 1322'
    N = 1000
    ALPHABET = range(57, 200)
    spectrum = string_to_spectrum(MASS_STRING)
    print(' '.join(map(peptide_pretty, noisy_cyclopeptides_with_spectrum(spectrum, N, alphabet=ALPHABET))))