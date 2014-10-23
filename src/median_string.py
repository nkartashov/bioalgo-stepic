__author__ = 'nikita_kartashov'

from utils.pyutils import top_by_snd_and_ignore
from utils.bioutils import all_possible_kmers, all_possible_kmers_from_text, hamming_distance


def median_string(dna_strings, k):
    all_kmers = all_possible_kmers(k)
    kmer_strings = [list(all_possible_kmers_from_text(string, k)) for string in dna_strings]

    def score_kmer_for_string(kmer, string_kmers):
        return min(hamming_distance(kmer, string_kmer) for string_kmer in string_kmers)

    def score_kmer(kmer):
        return sum(score_kmer_for_string(kmer, kmer_string) for kmer_string in kmer_strings)

    return top_by_snd_and_ignore(list((kmer, score_kmer(kmer)) for kmer in all_kmers))


if __name__ == '__main__':
    DNA_STRINGS = """CAATCAGCTCCGCGGATGTGACGGTCATTAGGAGATAAGTGA
ACCGCTTATATCGAATCAACTAACTTGTCTCTTGCGCAATTT
GTGCATGGTTCACGCACGGCATGGGCCATGTAATCACACGTC
AGAGTTACGAAAAGCAGCCACCGTAGCGACCAATCAGCAATA
TGGCGTCAATCATCGCAACGCGTTGACCGAGAAGTGTCGACA
CTAAATCCGATCCTTGATGAATCAGCCAAATGCGGCAAACGC
CTCGGAGCATTTTTCGCTAGATCCACTACGGAATCAGGGAGC
AATCCCTCATTGGAATCAGCCGGAACGGCGTCCAGTCGTCGT
TAATCATACAGCGTCTAGACGCTCGCTGGAATTGATGCGTTG
GATACTGCATAGACCCCTGTAATCCTTGTACAATCACTAGGA""".split()
    K = 6
    print(median_string(DNA_STRINGS, K))


