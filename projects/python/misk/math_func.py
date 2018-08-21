#!/usr/bin/python3
import math

def squ(x): return int(x) * int(x)

def hipo(A,B): return math.sqrt(squ(float(A)) + squ(float(B)))

def Carea(R): return math.pi * squ(R)
def cerc(D): return math.pi * D

def make_neg(X): return X - X*2
