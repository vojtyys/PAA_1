#!/usr/bin/python3
import re
from os import listdir, system, unlink

from os.path import isfile, join



def main():
    #remove prev outputs
    for f in listdir('./out/'):
        file = join('./out/', f)
        try:
            if isfile(file):
                unlink(file)
        except Exception as e:
            print(e)
    #run
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
