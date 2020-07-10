import itertools


def permutations_of(ls):
    """ Returns lexicographic permutations of all characters in ls"""
    return list(itertools.permutations(ls))


def main():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(permutations_of(digits)[1000000])


if __name__ == '__main__':
    main()
