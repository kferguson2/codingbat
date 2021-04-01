def make_abba(strA, strB):
    """ Given two strings, a and b, 
    return the result of putting them together in the order abba, 
    e.g. "Hi" and "Bye" returns "HiByeByeHi". """
    return strA + strB + strB + strA

print(make_abba('Hi', 'Bye')) # 'HiByeByeHi'
print(make_abba('Yo', 'Alice')) # 'YoAliceAliceYo'
print(make_abba('What', 'Up')) # 'WhatUpUpWhat'