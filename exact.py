#!/usr/bin/python3

#usage exact.py -time/-notime path_to_input_file
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
    combinations = itertools.product([0, 1], repeat=n) #generovani vsech kombinaci
    for x in combinations: #hledani nejlepsi kombinace
        bagWeight = 0
        bagPrice = 0
        for i in range(n):
            if not (x[i] == 0):
                bagWeight = bagWeight + weights[i]
                bagPrice = bagPrice + prices[i]
                if bagWeight > M:
                    break
        if bagWeight <= M and bagPrice > bestPrice:
            bestPrice = bagPrice
            #bestWeight = bagWeight
            bestCombination = x
    return bestPrice, bestCombination


def main():
    try: #otevreni vstupniho souboru
        f = open(argv[2])
    except IndexError:
        print('Invalid parameters')
        exit(1)
    except FileNotFoundError:
        print('File does not exist')
        exit(1)
    #nacteni a parsovani radku
    lines = f.readlines()

    for line in lines:
        words = line.split(' ')
        weights = []
        prices = []
        try: #prochazeni instanci a nacitani jejich dat
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
        start_time = time.time() #mereni casu reseni instance
        price, combination = solve(ID, n, M, weights, prices) #reseni instance
        if argv[1] == '-time': #vypis vysledku, pripadne casu
            stop_time = time.time()
            print("--- Instance %s completed, time %s seconds ---" % (ID, stop_time - start_time))
        print(ID, n, price, end=' ')
        for x in combination:
            print('', x, end='')
        print('')


if __name__ == '__main__':
    try: #kontrola parametru
        if argv[1] != '-time' and argv[1] != '-notime':
            print('Invalid parameters')
            exit(1)
    except IndexError:
        print('Invalid parameters')
        exit(1)
    start_time = time.time() #mereni celkoveho casu
    main()
    end_time = time.time()
    if argv[1] == '-time':
        print('Total time %s seconds' % (end_time - start_time))


