from sys import argv
from time import time

#usage heuristic.py -time/-notime path_to_input_file
ID_pos = 0
n_pos = 1
M_pos = 2
start_pos = 3

#kontrola parametru
def checkParam():
    try:
        if argv[1] != '-time' and argv[1] != '-notime':
            return False
        spam = argv[2]
    except IndexError:
        return False
    return True

#porovnavaci kriterium sortu
def getKey(elem):
    return elem[2]

#reseni
def solve(n, M, buffer):
    buffer.sort(key=getKey, reverse=True) #serazeni podle heuristiky
    bagWeight = 0
    bagPrice = 0
    usedItems = []
    for x in buffer: #pridavani polozek do zaplneni batohu
        if bagWeight + x[0] <= M:
            bagWeight = bagWeight + x[0]
            bagPrice = bagPrice + x[1]
            usedItems.append(x[3])
        else:
            break
    return bagPrice, usedItems


def main():
    #kontrola parametru, otevreni souboru
    if not checkParam():
        print('Invalid parameters')
        exit(1)
    try:
        f = open(argv[2])
    except FileNotFoundError:
        print('File does not exist')
        exit(1)
    #nacteni a parsovani souboru
    lines = f.readlines()

    for line in lines:
        words = line.split(' ')
        buffer = []
        try: #prochazeni a ukladani instanci
            ID = int(words[ID_pos])
            n = int(words[n_pos])
            M = int(words[M_pos])
            index = 0
            i = 0
            while i < 2 * n:
                weight = int(words[start_pos + i])
                price = int(words[start_pos + i + 1])
                buffer.append((weight, price, price / weight, index))
                i = i + 2
                index = index + 1
        except IndexError:
            print('Invalid data format')
            exit(1)
        except ValueError:
            print('Invalid data format')
            exit(1)
        start_time = time() #mereni casu reseni instance
        price, usedItems = solve(n, M, buffer) #reseni instance
        if argv[1] == '-time': #vypis reseni a popripade casu
            stop_time = time()
            print("--- Instance %s completed, time %s seconds ---" % (ID, stop_time - start_time))
        print(ID, n, price, end=' ')
        for x in range(n):
            if x in usedItems:
                print('', '1', end='')
            else:
                print('', '0', end='')
        print('')

if __name__ == '__main__':
    start_time = time()#mereni celkoveho casu
    main()
    if argv[1] == '-time':
        stop_time = time()
        print('Total time: %s seconds' % (stop_time - start_time))