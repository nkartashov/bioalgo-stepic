__author__ = 'nikita_kartashov'


def z_function(input_string):
    result = [0] * len(input_string)
    l = 0
    r = 0
    for i in range(1, len(input_string)):
        if i <= r:
            result[i] = min(r - i + 1, result[i - l])
        while i + result[i] < len(input_string) \
                and input_string[result[i]] == input_string[i + result[i]]:
            result[i] += 1
        if i + result[i] - 1 > r:
            l, r = i, i + result[i] - 1
    return result