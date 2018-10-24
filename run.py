#!/usr/bin/python3
import re
from os import listdir, system, unlink

from os.path import isfile, join
from sys import argv

outpath = ''

def main():
    #remove prev outputs
    if argv[2] == '-exact':
        for f in listdir('out_exact/'):
            file = join('out_exact/', f)
            try:
               if isfile(file):
                  unlink(file)
            except Exception as e:
                print(e)
    else:
        for f in listdir('out_heuristic/'):
            file = join('out_heuristic/', f)
            try:
               if isfile(file):
                  unlink(file)
            except Exception as e:
                print(e)
    #run
    instances = [f for f in listdir('inst/') if isfile(join('inst/', f))]
    for f in instances:
        if argv[2] == '-exact':
            outpath = re.sub('inst','out_exact',f)
            print('Running exact for %s' % f)
            system('python exact.py ' + argv[1] +' inst/' + f + ' > out_exact/' + outpath)
        else:
            outpath = re.sub('inst', 'out_heuristic', f)
            print('Running heuristic for %s' % f)
            system('python heuristic.py ' + argv[1] + ' inst/' + f + ' > out_heuristic/' + outpath)


if __name__ == '__main__':
    try:
        if (argv[1] != '-time' and argv[1] != '-notime') or (argv[2] != '-exact' and argv[2] != '-heuristic'):
            print('Invalid parameters')
            exit(1)
    except IndexError:
        print('Invalid parameters')
        exit(1)
    main()
