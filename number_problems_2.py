import math


def getFiveOrTens(num):
    fiveOrTens = {1 :"I",5 :"V",10 :"X",50 :"L",100:"C",500:"D",1000:"M"}
    return fiveOrTens[num]
    
def getOtherNums(num, pw):
    otherNums = { 2: [ getFiveOrTens(pw), getFiveOrTens(pw) ],
    3 : [ getFiveOrTens(pw), getFiveOrTens(pw), getFiveOrTens(pw) ],
    4 : [ getFiveOrTens(pw), getFiveOrTens(pw * 5) ], 
    6 : [ getFiveOrTens(pw * 5), getFiveOrTens(pw) ],
    7 : [ getFiveOrTens(pw * 5), getFiveOrTens(pw), getFiveOrTens(pw) ],
    8 : [ getFiveOrTens(pw * 5), getFiveOrTens(pw), getFiveOrTens(pw), getFiveOrTens(pw) ],
    9: [ getFiveOrTens(pw), getFiveOrTens(pw * 10) ] }
    
    ret = ""
    for each in otherNums[num]:
        ret += each
    return ret
    
def to_roman(number):
    if number <= 0 or number >= 5000:
        raise ValueError

    roman = ""

    i = 0
    while (10 ** i <= number):
        i += 1
    i -= 1
    
    powTen = 10 ** i
    while number != 0:
        try:
            roman += getFiveOrTens((number // powTen) * powTen) 
        except KeyError:
            roman += getOtherNums(number // powTen, powTen)
            
        number -= (number // powTen) * powTen;
    
        i -= 1
        powTen = 10 ** i
    
    return roman


def total_roman(n):
	pass

def chisel_strokes(n):
	pass

def describe(n):
	pass

def binary_without_zeros(n):
	pass
