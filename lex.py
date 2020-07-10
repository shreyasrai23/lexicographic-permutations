import sys

sys.setrecursionlimit(10**5)


class Permutation:

    perm_list = []

    def permute_string(self, str):
        """Return all permutations of the given list of digits"""
        if len(str) == 0:
            return ['']
        prev_list = self.permute_string(str[1:len(str)])
        next_list = []
        for i in range(0, len(prev_list)):
            for j in range(0, len(str)):
                new_str = prev_list[i][0:j] + str[0] + prev_list[i][
                                                       j:len(str) - 1]
                if new_str not in next_list:
                    next_list.append(new_str)
        return next_list


def factorial(n):
    """return the factorial of n"""
    r = n
    while n - 1 > 0:
        r = r * (n - 1)
        n = n - 1
    return r


def is_num(string):
    """Check if the given string contains numbers or not"""
    try:
        int(string)
    except ValueError:
        print("Please enter a string of digits")
        return False
    else:
        return True


def main():
    """ Calculates the nth term in the sequence of lexicographic
    permutations of a series of digits"""

    string = input("Enter a string of digits: ")
    while not is_num(string):
        string = input("Enter a string of digits: ")
    while True:
        try:
            index = int(
                input("Enter a number to signify which permutation to print "
                      "from the lexicographic order: "))
        except ValueError:
            print("Please enter a number only")
            continue
        else:
            p = Permutation()
            perms = p.permute_string(string)
            sorted_ls = []
            count = 0
            for str in sorted(perms):
                if count == int(index):
                    break
                sorted_ls.append(str)
                count += 1
            try:
                print(sorted_ls[index - 1])
            except IndexError:
                print(
                    "The series of digits you entered does not have this many "
                    "permutations")
                continue
            else:
                break


if __name__ == "__main__":
    main()


""" 
sample code:

Enter a string of digits: Hello there!
Please enter a string of digits
Enter a string of digits: 12345
Enter a number to signify which permutation to print from the lexicographic order: no
Please enter a number only
Enter a number to signify which permutation to print from the lexicographic order: 35
23514

"""