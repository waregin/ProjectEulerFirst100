# Triangle: T_n=n(n+1)/2        1, 3, 6, 10, 15, ...
# Square: Q_n=n^2               1, 4, 9, 16, 25, ...
# Pentagonal: P_n=n(3n - 1)/2   1, 5, 12, 22, 35, ...
# Hexagonal: H_n=n(2n - 1)      1, 6, 15, 28, 45, ...
# Heptagonal: S_n=n(5n-3)/2     1, 7, 18, 34, 55, ...
# Octagonal: O_n=n(3n-2)        1, 8, 21, 40, 65, ...

# triangle formula: 0.5 +- ((0.25 + (2 * x)) ** 0.5)
# square formula: x ** 0.5
# pentagonal formula: (1 +- ((1 + (24 * x)) ** 0.5)) / 6
# hexagonal formula: (1 +- ((1 + (8 * x)) ** 0.5)) / 4
# heptagonal formula: (3 +- ((9 - (40 * x)) ** 0.5)) / 10
# octagonal formula: (2 +- ((4 + (12 * x)) ** 0.5)) / 6
# x = n(2n - 1)
# x = 2n^2 - n
# 0 = 2n^2 - n - x
# (-b +- sqrt(b^2 - 4ac))/2a
# (1 + ((1 + (8 * x)) ** 0.5)) / 4


def is_valid_n(n):
    if type(n) is complex:
        return False
    return n > 0 and n % 1 == 0


def find_valid_n(n1, n2):
    if is_valid_n(n1):
        return int(n1)
    if is_valid_n(n2):
        return int(n2)
    return -1


def find_t_n(t):
    n1 = 0.5 + ((0.25 + (2 * t)) ** 0.5)
    n2 = 0.5 - ((0.25 + (2 * t)) ** 0.5)
    return find_valid_n(n1, n2)


def find_n_q(q):
    n = q**0.5
    return find_valid_n(n, -1)


def find_n_p(p):
    n1 = (1 + ((1 + (24 * p)) ** 0.5)) / 6
    n2 = (1 - ((1 + (24 * p)) ** 0.5)) / 6
    return find_valid_n(n1, n2)


def find_n_h(h):
    n1 = (1 + ((1 + (8 * h)) ** 0.5)) / 4
    n2 = (1 - ((1 + (8 * h)) ** 0.5)) / 4
    return find_valid_n(n1, n2)


def find_n_s(s):
    n1 = (3 + ((9 - (40 * s)) ** 0.5)) / 10
    n2 = (3 - ((9 - (40 * s)) ** 0.5)) / 10
    return find_valid_n(n1, n2)


def find_n_o(o):
    n1 = (2 + ((4 + (12 * o)) ** 0.5)) / 6
    n2 = (2 - ((4 + (12 * o)) ** 0.5)) / 6
    return find_valid_n(n1, n2)


def find_t_n(n):
    return int(n * (n + 1) / 2)


def find_q_n(n):
    return n**2


def find_p_n(n):
    return int((n * ((3 * n) - 1)) / 2)


def find_h_n(n):
    return n * ((2 * n) - 1)


def find_s_n(n):
    return int((n * ((5 * n) - 3)) / 2)


def find_o_n(n):
    return n * ((3 * n) - 2)
