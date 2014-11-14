__author__ = 'nikita_kartashov'

from utils.bioutils import all_possible_kmers_from_text
from utils.pyutils import head, last, init, tail


def get_start(kmer):
    return init(kmer)


def get_end(kmer):
    return tail(kmer)


def debruijn_graph(string, k):
    kmers = list(all_possible_kmers_from_text(string, k))
    kmers_in_graph = []
    adjacency_lists = []
    for kmer in kmers:
        start = get_start(kmer)
        end = get_end(kmer)
        if not start in kmers_in_graph:
            kmers_in_graph.append(start)
            adjacency_lists.append([])
        if not end in kmers_in_graph:
            kmers_in_graph.append(end)
            adjacency_lists.append([])
        start_index = kmers_in_graph.index(start)
        end_index = kmers_in_graph.index(end)
        adjacency_lists[start_index].append(end_index)
    return '\n'.join(
        sorted('{0} -> {1}'.format(kmers_in_graph[start_index],
                                   ','.join(sorted(kmers_in_graph[end_index] for end_index in end_list))) for
               start_index, end_list in enumerate(adjacency_lists) if end_list))


if __name__ == '__main__':
    K = 10
    TEXT = 'CGCTTCTACACTGGCTTGAAATCCCAAGCACCATACGTCTTCTGTAACGCATGTGGAGTACGGGCCCATTGCTTGCATAGACGGGGCATTCCTGTAGCTATCACACAATCTCATCGACAATCGCGGCTGACAAGATGTAAGAATTTCAACGAATTACTTTGACAACATTACATTCTCCACCAGTGACGCACTGAGTCCACGAGGAAGATGAGTATAAATAGAGGCGTACGATCTAGAGCATAGGTTGCCTCCATCGAAGGCGCGGTGCACAGTATCTAGGTAGACCTTTCACGCGTAGCAGAGTGAGATGTTAAGATGTGGTAGATACCAGTGCCGCGCACACCCCTTCAAAGTCAATACGAATTGTATCTAGAAACAAGCACACAAGTCACTGCCGCGTGCGCTTGATGAGGTGGTGATCTTGCTAGTTAAGTGCGGTAAGTCAGCTATTTCTAGCCCGTTCAACGTCTATATCAGGTGGGGAATACCCAGTTAAAGATTGAAGGTTAGGCTAGGCGTAGTGCGCGTAGACCCGTAGATCGCTGTCTACTCCCTTACGCGGAATAAATCCTTCGTCCGGCGAGTGCTGCAATTCCATTGTCCTCATCGCAGACGGAACAGTCCAGAGCGATACTTTGGTACCTTGATTGCATTAATCCGTCGATTGGACCTGAGATTGAATAGGCCGATGGTCATACGGTCGTACCAGTACGAGGACTGGGTGCCCCAGCTTGAATGAGGATGCGGATGAACTCTTACCTACGCATGGTGATCTAGGCCGTATGTTTGCGGCCCCCCGGGCGGACAGCTCACCTAGCACAAACGAGTGGGCTTGGTTTTTCTCCGCAGCACGCACTGCATAGGGGGGTTCATAGAAGGAGCAATAAC'
    print(debruijn_graph(TEXT, K))
