__author__ = 'nikita_kartashov'

from utils.pyutils import last
from peptide_spectrum import spectrum_from_mass_string

from peptides_with_given_mass import AMINO_ACIDS_WITH_MASS

AMINO_ACIDS = AMINO_ACIDS_WITH_MASS.keys()


def string_to_spectrum(string):
    return list(map(int, string.split()))


def peptide_pretty(peptide):
    return '-'.join(map(str, peptide))


def cyclopeptides_with_spectrum(model_spectrum):
    sorted_model = sorted(model_spectrum)
    null_peptide = []
    peptide_list = [(null_peptide, 0)]
    result = []
    while True:
        if len(peptide_list) == 0:
            break
        new_list = []
        for peptide, mass in peptide_list:
            for aa in AMINO_ACIDS:
                new_peptide = peptide + [aa]
                new_mass = mass + aa
                if new_mass in model_spectrum:
                    if last(model_spectrum) == new_mass:
                        if sorted(spectrum_from_mass_string(new_peptide)) == sorted_model:
                            result.append(new_peptide)
                    else:
                        new_list.append((new_peptide, new_mass))
        peptide_list = new_list
    return result


if __name__ == '__main__':
    STRING_SPECTRUM = '0 87 87 101 103 113 128 129 129 156 156 190 216 229 232 241 243 243 257 258 269 319 342 344 345 346 356 361 372 385 397 448 448 459 472 473 475 484 498 498 501 535 585 585 587 588 601 602 604 604 654 688 691 691 705 714 716 717 730 741 741 792 804 817 828 833 843 844 845 847 870 920 931 932 946 946 948 957 960 973 999 1033 1033 1060 1060 1061 1076 1086 1088 1102 1102 1189'
    spectrum = string_to_spectrum(STRING_SPECTRUM)
    print(' '.join(peptide_pretty(cyclopeptides_with_spectrum(spectrum))))
