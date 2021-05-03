#!/usr/bin/env python3

import random
from TACsanitizer import randTAC, anyTAC, realTAC, selectTAC

###Main for Testing###
def main():
    exvar = False
    query = input('IMEI type [-h or help]: ')
    if str(query).lower() == 'help' or str(query).lower() == '-h':
        print('  ├  no input -- all')
        print('  ├ \"real\" -- only real TAC codes')
        print('  ├  phone/brand -- only matching TAC codes')
        print('  └ \"exit\" -- exit script')
        main()
        exit()
    if str(query).lower() == 'quit' or str(query).lower() == 'exit':
        exvar = True
    if not exvar:
        imei = newIMEI(query)
       #print(imei)
        luhn = luhnDigit(imei)
       #print(luhn)
        totalIMEI = str(imei)+str(luhn)
        print(totalIMEI)
       #print(generateIMEI())
        main()

###Generator###
def generateIMEI(query):
    imei = newIMEI(query)
    luhn = luhnDigit(imei)
    return str(imei), str(luhn)


###Generate New IMEI Value###
def newIMEI(query):
    #                                  luhn      SVN
    # IMEI format:                        \      /
    # [ aa - bb - bb - bb - cc - cc - cc - d / ee ]
    # [ TAC          |FAC | Serial Numbr | Luhn   ] <- Old IMEI
    # [ TAC               | Serial Numbr | Luhn   ] <- New IMEI
    # [ TAC          |FAC | Serial Numbr | SVN    ] <- Old IMEI/SV
    # [ TAC               | Serial Numbr | SVN    ] <- New IMEI/SV

    if not query:
        TAClist = anyTAC()
    elif str(query).lower() == 'real':
        TAClist = realTAC()
    else:
        if isinstance(selectTAC(query), list):
            TAClist = selectTAC(query)
        else:
            print(f'[ERROR] {selectTAC(query)}')
            main()
    imei = ''
    imei += str(randTAC(TAClist))
    for i in range(6):
        imei += str(random.randint(0,9))
    return imei

###Generate Luhn Digit###
def luhnDigit(imei):

    imei = list(str(imei))
    set1 = ''
    set2 = ''

    ###Seperate into 2 Groups###

    switcher = True
    for i in imei:
        if switcher:
            set1 += i
        else:
            set2 += i
        switcher = not switcher

    ###Calculate Luhn Digit###

    set1 = list(set1)
    set2 = list(set2)
    tempSet1 = []
    
    for i in range(len(set2)):      # double each digit in set 1
        set2[i] = int(set2[i])*2    # convert to int

    for i in range(len(set2)):      # break down set 1
        set2[i] = str(set2[i])      # into individual
        tempSet = list(set2[i])     # digits
        for i in tempSet:
            tempSet1.append(i)
    set2 = tempSet1
    
    for i in range(len(set1)):      # convert lists
        set1[i] = int(set1[i])      # to int format
    for i in range(len(set2)):      # from string
        set2[i] = int(set2[i])
    
    for i in set2:                  # combine lists
        set1.append(i)              # into one list
    total = 0
    for i in set1:                  # add lists together
        total += i

    if total%10 == 0:               # calculate luhn
        return total%10             # digit
    else:
        return 10-(total%10)



if __name__ == '__main__':
    main()

