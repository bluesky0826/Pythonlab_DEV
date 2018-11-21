#!/usr/bin/env python
#coding:utf-8

def convert(func, seq):
    'conv. sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = (123, 45,67, -6.2e8, 999999999L)
print convert(int, myseq)
print convert(long, myseq)
print convert(float, myseq)


'''
[123, 45, 67, -620000000, 999999999]
[123L, 45L, 67L, -620000000L, 999999999L]
[123.0, 45.0, 67.0, -620000000.0, 999999999.0]
'''