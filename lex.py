# A recursive program that will produce any given lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
import sys

sys.setrecursionlimit(10**5)

reference = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ls = []

def factorial(n):
    r = n
    while((n-1) > 0):
        r = r * (n-1)
        n = n-1
    print(r)
    return r



# Calculates any lexicographic permutation for a given number of digits that are lexicographically ordered starting from 0 and populates an empty list with the result
def calculateterm(n, termx):
    numTerms = factorial(n)
    termsperset = factorial(n-1)
    setDigit = 0

    for x in range(0, n):
        if termx > termsperset:
            termsperset = termsperset + termsperset
            setDigit = setDigit + 1
    ls.append(setDigit)
    if n > 0:
        calculateterm(n-1, termx)
    else:
        print(ls)
        return ls

calculateterm(10, 1000000) # Calculates the millionth term in the sequence of lexicographic permutations of the digits 0 to 9