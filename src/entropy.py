__author__ = 'nikita_kartashov'

from math import log2

from utils.pyutils import transpose


def column_entropy(column):
    def probability_entropy(probability):
        return 0 if probability == 0 else probability * log2(probability)

    return -sum(map(probability_entropy, column))


def matrix_entropy(matrix):
    columns = transpose(matrix)
    return sum(map(column_entropy, columns))


if __name__ == '__main__':
    ENTROPY_TABLE = """.2  .2   0   0   0   0  .9  .1  .1  .1  .3   0
.1  .6   0   0   0   0   0  .4  .1  .2  .4  .6
0   0   1   1  .9  .9  .1   0   0   0   0   0
.7  .2   0   0  .1  .1   0  .5  .8  .7  .3  .4  """
    probability_rows = (map(float, line.split()) for line in ENTROPY_TABLE.split('\n'))
    print(matrix_entropy(probability_rows))
