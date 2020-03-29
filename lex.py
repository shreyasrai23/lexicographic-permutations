# A recursive program that will produce any given lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9

ls = []

def factorial(n):
    r = n
    while((n-1) > 0):
        r = r * (n-1)
        n = n-1
    return r


# Calculates any lexicographic permutation for a given number of digits that are lexicographically ordered starting from 0 and populates an empty list with the result
def calculateterm(n, termx):
    numTerms = factorial(n)
    termsperset = factorial(n-1)
    setnum = 0

    for x in range(n):
        if termx > termsperset:
            termsperset = termsperset * 2
            setnum = setnum + 1
    ls.append(str(setnum))
    calculateterm(n-1, termx)

    print(ls)
    return ls

calculateterm(10, 1000000) # Calculates the millionth term in the sequence of lexicographic permutations of the digits 0 to 9