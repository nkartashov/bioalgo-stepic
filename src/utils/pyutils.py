__author__ = 'nikita_kartashov'

from functools import reduce
from itertools import chain, islice
from operator import mul


def sliding(string, k):
    if len(string) < k:
        return []
    else:
        return [string[i:i + k] for i in range(len(string) - k + 1)]


def split(input_string, every):
    return [input_string[start:start + every] for start in range(0, len(input_string), every)]


def fst(x):
    return x[0]


def snd(x):
    return x[1]


def last(x):
    return x[len(x) - 1]


def sort(data, by_fun=lambda x: x, descending=False):
    return sorted(data, key=by_fun, reverse=descending)


def sort_by_snd(data, descending=False):
    return list(sort(data, by_fun=snd, descending=descending))


def filter_between(data, bot, top, by_fun=lambda x: x):
    return filter(lambda x: by_fun(x) < top, filter(lambda x: by_fun(x) >= bot, data))


def top(data, by_fun=lambda x: x, n=1, descending=False):
    return list(islice(sort(data, by_fun=by_fun, descending=descending), n))


def top_by_snd(data, n=1, descending=False):
    return top(data, snd, n, descending)


def topt_by_snd(data, t):
    return list(filter(lambda x: snd(x) <= t, data))


def read_file_into_string(file):
    with open(file) as f:
        return f.read()


def top_by_snd_and_ignore(data, n=1, descending=False, with_ties=False):
    if not data:
        return []
    data = list(data)
    threshold = snd(min(top_by_snd(data, n=n, descending=descending), key=snd))

    def inner(x):
        param = snd(x)
        return param < threshold if not descending else param > threshold

    filter_fun = inner
    final_filter_fun = filter_fun
    if with_ties or n == 1:
        def new_inner(x):
            return filter_fun(x) or snd(x) == threshold

        final_filter_fun = new_inner
    return list(map(fst, filter(final_filter_fun, data)))


def flatten_to_list(l):
    return list(chain.from_iterable(l))


def flatten_to_set(l):
    return set(chain.from_iterable(l))


def transpose(l):
    return [list(x) for x in zip(*l)]


def product(l):
    return reduce(mul, l)


def tail(l):
    return l[1:]