__author__ = 'nikita_kartashov'

from profile_most_probable_kmer import NUCLEOTIDES_FOR_PROBABILITIES, most_probable_kmer
from utils.pyutils import transpose, top_by_snd_and_ignore, fst, tail
from utils.bioutils import hamming_distance, all_possible_kmers_from_text


def consensus(matrix):
    columns = transpose(matrix)

    def column_consensus(column):
        return fst(top_by_snd_and_ignore(((nucleotide, column.count(nucleotide))
                                          for nucleotide in column), descending=True))

    return [column_consensus(column) for column in columns]


def matrix_score(matrix):
    consensus_string = consensus(matrix)
    return sum(hamming_distance(consensus_string, string) for string in matrix)


def build_profile_columns(motifs):
    columns = transpose(motifs)

    def column_probabilites(column):
        return [column.count(nucleotide) * 1.0 / len(column) for nucleotide in NUCLEOTIDES_FOR_PROBABILITIES]

    return [column_probabilites(column) for column in columns]


def greedy_motif_search(dna_strings, k, profile_builder=build_profile_columns):
    best_motifs = [dna_string[:k] for dna_string in dna_strings]
    for kmer in all_possible_kmers_from_text(fst(dna_strings), k):
        current_score = matrix_score(best_motifs)
        motifs = [kmer]
        for dna_string in tail(dna_strings):
            profile = profile_builder(motifs)
            additional_motif = most_probable_kmer(dna_string, k, profile)
            motifs.append(additional_motif)
        if current_score > matrix_score(motifs):
            best_motifs = motifs
    return best_motifs


if __name__ == '__main__':
    DNA_STRINGS = """AATAAACGTATAGGACTTGGCGTTATCCTGCGGTTCGGATTGACCACATTGGAGACAATCTCGAAGCTGATGCGGATGCTGGCCCAAAGGACGGTGTGTATGGTGGGCGCTCATGCGTGCATCCATGAATTATCCGCAGCCGAATCCGTATCGTAA
ATAGCTTTAACAACCCTGCGTTACGCACCAGTTATATTGATGTCGTAATCAAGTTTGCCGCGATTGACCGTACCCAGTCACGAATCTACGAATACCAAAACGATACCACCTGCAAAGACCCCGAAACAATTGAAGACTACCACGGCAGCGGGGAAG
TTTCTGAGCGTGACACCTGACGCGCTATCTTACCCCGTGGGTCGACATCAAAGCCTCCACAGCCTGGGCTGCTCTTATGACAGTATCTGGCATAATAGCCCCTAGCCGCTTCGTGATGAATGCTCATCGTTCGTCACCGTCCTAACCAGAGGCAAA
CCTGAGATTGACCAAGTCGGACGGACTGATAAAGCATAGTGCGTTCAACAACGCTCCTCGTCACACTAATGTCACGTCGTCAACAGCTATAACAAGAACCTGTGCTTCCATCTCGAGTTTAAGTATACGGGTTCTGGCAGAACTATAAAAACATGG
GGAGGGGGACGACCACCTTGAGAAAACCTGCGATACGAGACGCTTTGTGCATGTGTAACCGGCCCCCGTTGACCTCTACCTCTGACACGGGCATTTGAGCTCACCGAGTGTCAAGCTTGCGCTCTGTGCCATTGCCTATACCAAGCGTTGGTGGCA
TTGCCCAAGTAACCTGTTCTTGGAGAGTCGGTACTCCGTCGTAATGCAGGGTCACAAGGCCCATTAAGCAAGAGGGAATAGATTGCCAATCAGTTTGAGTCGGAAGCATACAGGATTCAGGACCACCACTCCACCCTGCGCTTCTTTCACTACAAG
CATTCTATAAGCAGGGGTCCTTGAGCTTGCAGAGTTTCGGTTGTCCAACCGTCACTATAGGTAGGAGCTATGAAGGGTCTTCCACTGTATAACTAGACCCTGGGTTACCAGTCGCGTCCCCGGAGAACGGTTTTCCAGGTACCATAGCTGTTTGGC
ACACAGAGCATCCCCGGGACTATTGAGCAAGTCGCCCAAGAGTGAACTCGTCGCGACGCCTCCCCCGCGACATCCAAGTATTTTACATTCCTCATTAACAGGGCTCCAGCAGCCTCGCGAAGGACTGGTGTGCGAAAGTTTTGCATCCTGCGCTCC
CATGTGCGGATTGCTCACTCTTGTGCCTCAACAATCTCTATCTGTGCAGAAACAACCACCCACGACCCCTCAGCGTAGTTTAGCTGACGCGGGGCCGGAGTGACGGCTCCGAAGGACTGTACCCTGGGCTCCCCAGATCCAAAGTAAATGCTTAAG
GCTACAGAAGGAATACAATGGGTGCGCGCCCGACTCCAACCTATCATTACCCTGCGTTGCGTAAAACGCCACCTAACCCGTCGTGGTACCTCTGAAAGTTGCCGGTCGAAACGTAGATCGGGGTATCTGAGGTGCGACTGTTGGGTTTTGCCTCAG
GCAACGGGCACGTTCAAGTTGCCTGTATGCGACTAGCTTAGAAAGAGTTAAGGTAACCGGCCGAACGACTGAAACCTGCGGTACGGATCCAATTCGGCCAGGTGAATGGCTGAAATGATAGTATCGGCATGGCCAGAAAGTCCTCCACCTTAGCTC
AACCTGCGGTGCTACTACACAGAATAGTCGACAGCTAGACCTGTGCGGTCTTTTCTAATGCGGTCCCGCCTTCTATCAATACGGCCGTCAAAGTCCGAGTTGGTGTAGTCTCACAGGTTCGTGGTGTTAGATACCGCGGAGTCTGGGCAGCACAAG
GTGGGCAGGTCGGCCGCCGAAGAGAAGGATACGGGTGGTTCGGCACGACGAAGAACAGAGCAGTATACAGTAATCCTGGGATTCGGGGATATAATAAGTCCGGTAGATGTTCCCTCGCCACGTGGAGTCGACTGGCGGTCGGCTTCTTGGGTTCAA
AGCCTGTGATGCACATAATCGTTTGCATATTGTAGTGTTGTAAACGACGCGCTGGCACCCGGATCGGGATCGCTCAACCCTTATTGTATTTGTTTTCAAGACGGGTCTTTCCCACGTACGGATACGCCTCAACACCGTCGATGGACTCCATGACGT
ATAAGATGGCATGACCGGATATTGTCTAAATCTATGTGTGGGAGCTATAGCGCAAATGCGCAAATGAAGAAAGTATTCAAGATTAGCCTGAGATCCGAAAGCTATGTTCGTGCCTTCCGCATGTATGGTCCTGTTCTTAAAGCCCGTTTACCCAAA
TAGTTCTCACTAAGATTTCCCTGGAAAGCCGTGACGCAGAGCACGTAACCAACTACGAGCTAGTTTTCCTTAGTCGGGGCCTTTATCCTGGGGTACATTCCAGATCACTGGGCTTCCGATGCTCGTATTGCGCAAAGCACATAGCAAGGATTCGGT
TAAAGATAACAAGTCCGGCAGGTACGTGTACATATGTTACGAACCGTGTGGCAACACGTTAGACGTGGATACGTGCACTTATTGCCGCGTTGCCGTTTCGTTAACGCAAAGAATTGGAGGCCATCTGCGACCCCTTCAGTTTCGAACCTGTGCTTC
TAATGCTACCCGGCAAATCTGCGGATACCTCCCTGAGAGTCGTCGAGTGCCGGTCATGGCGTCCGCAGGGGTTATGCTATTATCTTCCGTATTAACTTATTAAACGCTTATTCGGTTGAAACCGGCGGGATCAACCTGGGATCCAACAGTTTAGCA
CCTGCTGCTGAAAACCTGAGATCCTAGTCTGAGGTACACGGCCTCCCAACTATAAACGCACGCAAGGAACCCCGTAGTCATTTTTCCATGGTACTAGACAATAGTGACCGGCGTAATTGCACGGGCCTCTCATCGGTACGGGTCGAGCTGGTCTAT
TATGGTGTTGTTAAGGCTAAACAGGCAATGGGACCGTACCCGGACACCTCAGAGGTGTCTAATGCGCAACGTGGTGCTCCCAAAAGGGCCAAGTTGAACCTGAGCTCCTTCTGTTATAAATCCGGCTATTGAGATAAAAATAATCAACTACAAGCT
TGGACCACTAGAGACATGACGCCTGAGGTCGTTGCCGACCTACAGGTCAGCGGCACTAGGCTGACTGCGCCCTGTCGATTTGTTAACGACAGACACGAGTTGCCCGACTGGTATGGTTCAGATCCACATGCAACTGAATACTCAAACCTGGGCTTC
GCCTACGGAATCCTGGTCCTTCTCGGCGGAGAGACTGCGCTTGAACTCTCAGCGCCCAACTGGTACATAGAAGCTGACTGCTCGCCTGTGACGAACCACTCCGTCTGACTCAACGGTCAGAACAGGCATGCCAACCTGTGATACGTTATCAAGCAA
GCTTGCAGTTGGACCCTGCGGTACAACCAGTTGAAGCGAAGACGGACCGAGAGCTCGCAAATAATTGGTGATGGGCTGCTAGCGCCGCGTATGTTGTCTAGGTAGGTAATGCCGGTTTCGCCGGGGCCGTCCTCACCGTAGCATGCTTAAGTTTCC
CTTAGGTCAAATCTTAAGGCGATTAATTTCACTCGTTGCTCGAAGAGACGTTCTACTTTGGTGCTGCGTCTAAGAGAGATTTTGACCCAGTGATGCAACCTGGGCTACCTTTCAAGTTATTCTCGTTATTGACTCGATGACGAAACGAATTCAGGT
GACGCGCTGGCCACAAACGCACCCTATCTGTTTACATTCGTGGATGTAATGTTCGCGCTATAGCAAGATATTGCAAAACTCGAGCCTCTTGAGGATTACTGAAGGCCGGATCCGAAGGTAACCCTGAGGTCCGCGGACCATGGGATCTCCGAAGTG""".split()
    K = 12
    print('\n'.join(greedy_motif_search(DNA_STRINGS, K)))
