__author__ = 'nikita_kartashov'

from collections import Counter

from cyclopeptide_sequencing import peptide_pretty, string_to_spectrum, AMINO_ACIDS, spectrum_from_mass_string
from utils.pyutils import last, top_by_snd_and_ignore


def noisy_cyclopeptides_with_spectrum(model_spectrum, n, alphabet=AMINO_ACIDS):
    model_set = Counter(model_spectrum)

    def score(spectrum):
        return len(list((model_set & Counter(spectrum)).elements()))

    peptide_mass = max(model_spectrum)
    null_peptide = []
    peptide_list = [(null_peptide, 0)]
    top_peptides = None
    top_score = 0
    while True:
        if len(peptide_list) == 0:
            break
        new_list = []
        for peptide, mass in peptide_list:
            for aa in alphabet:
                new_peptide = peptide + [aa]
                new_mass = mass + aa

                if not new_mass > peptide_mass:
                    new_score = score(spectrum_from_mass_string(new_peptide))
                    if new_mass == peptide_mass:
                        if new_score > top_score:
                            top_peptides = [new_peptide]
                            top_score = new_score
                        elif new_score == top_score:
                            top_peptides.append(new_peptide)

                    new_list.append(((new_peptide, new_mass), new_score))
        peptide_list = top_by_snd_and_ignore(new_list, n=n, descending=True, with_ties=True)
    print(len(top_peptides))
    return top_peptides

if __name__ == '__main__':
    STRING_SPECTRUM = '0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322'

    N = 1000
    spectrum = string_to_spectrum(STRING_SPECTRUM)
    print(' '.join(map(peptide_pretty, noisy_cyclopeptides_with_spectrum(spectrum, N))))
