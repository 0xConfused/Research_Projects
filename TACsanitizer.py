#!/usr/bin/env python3

import re
import random

### Sanitize TAC List ###
TACSOURCE = 'C:/Users/******/*******/*****/********/******/********-**/********/**** *******/TACcodes.txt'

def anyTAC():
    TACcodes = open(TACSOURCE,'r')
    TAClist = []
    for line in TACcodes:
        TAC = re.findall('\d{8}', line)
        TAClist.append(TAC[0])
    TACcodes.close()
    return TAClist

def randTAC(TAClist):
    rand = random.randint(0,len(TAClist)-1)
    return TAClist[rand]

def realTAC():
    TACcodes = open(TACSOURCE,'r')
    TAClist = []
    for line in TACcodes:
        if not re.search('^.*fake TAC codes', line, re.IGNORECASE):
            TAC = re.findall('\d{8}', line)
            TAClist.append(TAC[0])
    TACcodes.close()
    return TAClist

def selectTAC(query):
    TACcodes = open(TACSOURCE,'r')
    TAClist = []
    for line in TACcodes:
        if re.search(' [\W\D]*'+query+'( |\D{1,2})[\W\D]*', line, re.IGNORECASE):
            TAC = re.findall('\d{8}', line)
            TAClist.append(TAC[0])
    TACcodes.close()
    if len(TAClist) == 0:
        return 'No results found in query for \''+ query +'\''
    else:
        return TAClist


### Main for Testing ###
def main():
    testval = input('input testval here: ')
    if testval == 'quit' or testval == 'exit':
        exit()
    print(selectTAC(testval))
    main()
    exit()

if __name__ == '__main__':
    main()
