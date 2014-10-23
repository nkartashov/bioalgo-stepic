__author__ = 'nikita_kartashov'

from functools import reduce

AMINO_ACIDS_WITH_MASS = {57: 1, 71: 1, 87: 1, 97: 1, 99: 1, 101: 1, 103: 1, 113: 1, 114: 1, 115: 1, 128: 1, 129: 1,
                         131: 1, 137: 1, 147: 1, 156: 1, 163: 1, 186: 1}


def proteins_with_mass(mass):
    memory = [0] * (mass + 1)
    memory[0] = 1

    def inner(mem, i):
        for amino_mass, protein_number in AMINO_ACIDS_WITH_MASS.items():
            residual_mass = i - amino_mass
            if residual_mass >= 0:
                mem[i] += mem[residual_mass] * protein_number
        return mem

    reduce(inner, range(1, mass + 1), memory)

    return memory[mass]


if __name__ == '__main__':
    MASS = 1203
    print(proteins_with_mass(MASS))