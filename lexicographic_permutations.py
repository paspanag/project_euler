from itertools import permutations

def permutation_to_number(perm_tup):
    mult = 1
    sum_digits = 0
    # ordering here dont matter, the permutations for reveresed and forward are represented
    for n in perm_tup:
        sum_digits += n*mult
        mult *= 10

    return sum_digits



if __name__ == "__main__":
    combos = [0,1,2,3,4,5,6,7,8,9]

    all_combos = [ permutation_to_number(x) for x in permutations(combos, 10) ]
    answers = sorted(all_combos)
    print answers[999999]
    print answers[0]
    print answers[1]
    print answers[2]
    print answers[3]
