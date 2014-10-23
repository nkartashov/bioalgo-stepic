__author__ = 'nikita_kartashov'


def skew(text):
    def skew_mapper(letter):
        if letter == 'G':
            return 1
        elif letter == 'C':
            return -1
        else:
            return 0

    mapped_text = map(skew_mapper, text)
    current_value = 0
    result = [current_value]
    for value in mapped_text:
        current_value += value
        result.append(current_value)

    return result

if __name__ == '__main__':
    TEXT = 'GAGCCACCGCGATA'
    print(' '.join(map(str, skew(TEXT))))
