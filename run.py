#!/usr/bin/python3
import re
from os import listdir, system

from os.path import isfile, join



def main():
    instances = [f for f in listdir('./inst/') if isfile(join('./inst/', f))]
    for f in instances:
        outpath = re.sub('inst','out',f)
        checkpath = re.sub('inst', 'sol', f)
        #print(outpath)
        #print(checkpath)

        system('./paa_1.py -notime inst/' + f + ' > ./out/' + outpath)
        system('diff ./out/' + outpath + ' ./sol/' + checkpath)
        #print(f)

if __name__ == '__main__':
    main()
