def collatz_s(n, acc=[]):
    acc.append(n)
    if n == 1:
        return len(acc), acc
    if n % 2 == 0:
        return collatz_s(n/2,acc)
    else:
        return collatz_s(3*n+1,acc)

def collatz(n,prog_n=None,count=0):
    prog_n = prog_n if prog_n else n
    count += 1
    if prog_n == 1:
        return count, n
    if prog_n % 2 == 0:
        return collatz(n,prog_n=prog_n/2,count=count)
    else:
        return collatz(n,prog_n=3*prog_n+1,count=count)

def cache_check(n, cache):
    try:
        return cache[n]
    except KeyError:
        return False

def collatz_mem(n, count=0, n_prog=None, cache=None):
    n_prog = n_prog if n_prog else n
    cache = cache if cache else {}
    count = count + 1
    if n_prog == 1:
        cache[n] = count
        return count, n, cache
    else:
        cache_value = cache_check(n_prog, cache)
        if cache_value:
            return count + cache_value, n, cache

    if n_prog%2 == 0:
        return collatz_mem(n, count=count, n_prog=n_prog/2, cache=cache)
    else:
        return collatz_mem(n, count=count, n_prog=3*n_prog+1, cache=cache)

if __name__ == '__main__':
    # import sys
    # length, sequence = collatz(int(sys.argv[1]))
    # print("count: {0}, \n start: {1}".format(length,sequence))
    # print max([ collatz(x,acc=[])[0] for x in range(1,999999)])
    # largest = 0
    # n_largest = 0
    # for i in range(1,1000000):
    #     count, n = collatz(i)
    #     if count > largest:
    #         largest = count
    #         n_largest = n
    #
    # print("largest count: {0} using starting value {1}".format(largest,n_largest))

    cache = {}
    largest = 0
    largest_n = 1
    for i in range(1,1000000):
        count, n, cache = collatz_mem(i,cache=cache)
        if count > largest:
            largest = count
            largest_n = n

    print("largest count: {0} using starting value {1}".format(largest,largest_n))

    # print max([ collatz(x,acc=[])[0] for x in range(1,999999)])
    # for i in range(1,1000000):
    #     length, sequence = collatz(i,acc=[])
    # #     print length
    #     if length > 500:
    #         print("Length: {0}, \n sequence: \n {1}".format(length,sequence[0]))
