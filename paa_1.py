#!/usr/bin/python3
import itertools
import time
from sys import argv

ID_pos = 0
n_pos = 1
M_pos = 2
start_pos = 3

def solve(ID, n, M, weights, prices):
    #bestWeight = 0
    bestPrice = 0
    bestCombination = []
    combinations = itertools.product([0, 1], repeat=n)
    for x in combinations:
        bagWeight = 0
        bagPrice = 0
        for i in range(n):
            if not (x[i] == 0):
                bagWeight = bagWeight + weights[i]
                bagPrice = bagPrice + prices[i];
                if bagWeight > M:
                    break
        if bagWeight <= M and bagPrice > bestPrice:
            bestPrice = bagPrice
            #bestWeight = bagWeight
            bestCombination = x
    return bestPrice, bestCombination


def main():
    try:
        f = open(argv[1])
    except IndexError:
        print('File does not exist')
        exit(1)

    lines = f.readlines()

    for line in lines:
        words = line.split(' ')
        weights = []
        prices = []
        try:
            ID = int(words[ID_pos])
            n = int(words[n_pos])
            M = int(words[M_pos])
            i = 0
            while i < 2*n:
                weights.append(int(words[start_pos + i]))
                prices.append(int(words[start_pos + i + 1]))
                i = i + 2
        except IndexError:
            print('Invalid format')
            exit(1)
        except ValueError:
            print('Invalid format')
            exit(1)
        start_time = time.time()
        price, combination = solve(ID, n, M, weights, prices)
        print("--- %s seconds ---" % (time.time() - start_time))
        print(ID, n, price, end='')
        for x in combination:
            print(' ', x, end='')
        print('')


if __name__ == '__main__':
    main()



