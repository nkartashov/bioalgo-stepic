__author__ = 'nikita_kartashov'

from utils.pyutils import flatten_to_list

AMINO_ACID_MASS = {'G': 57,
                   'A': 71,
                   'S': 87,
                   'P': 97,
                   'V': 99,
                   'T': 101,
                   'C': 103,
                   'I': 113,
                   'L': 113,
                   'N': 114,
                   'D': 115,
                   'K': 128,
                   'Q': 128,
                   'E': 129,
                   'M': 131,
                   'H': 137,
                   'F': 147,
                   'R': 156,
                   'Y': 163,
                   'W': 186}


def subpeptides(protein_string, subpeptide_string_length):
    string_for_subpeptides = protein_string + protein_string
    return [string_for_subpeptides[i: i + subpeptide_string_length] for i in range(len(protein_string))]


def protein_mass(protein):
    return sum(map(lambda aa: AMINO_ACID_MASS[aa], protein))


def spectrum_from_mass_string(mass_string):
    spectrum = [0]
    spectrum.extend(
        list(map(sum, flatten_to_list(subpeptides(mass_string, i) for i in range(1, len(mass_string))))))
    spectrum.append(sum(mass_string))
    return spectrum


def spectrum_from_protein(protein_string):
    return spectrum_from_mass_string(map(lambda aa: AMINO_ACID_MASS[aa], protein_string))


if __name__ == '__main__':
    PROTEIN = 'YSPDDQACQCHMQC'
    print(' '.join(map(str, spectrum_from_protein(PROTEIN))))





