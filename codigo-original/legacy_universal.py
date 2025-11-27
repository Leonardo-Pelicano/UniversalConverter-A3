
# legacy_universal.py - intentionally messy monolith combining temperature, length and weight conversions
# This file is the "original" bad code students received.
import sys, math, time, random

def conv_temp(v, f, t):
    try:
        v = float(v)
    except:
        print("bad")
        return None
    if f == 'c':
        if t == 'f':
            return v * 9/5 + 32
        if t == 'k':
            return v + 273.15
        if t == 'r':
            return (v + 273.15) * 9/5
        if t == 'c':
            return v
    if f == 'f':
        if t == 'c':
            return (v - 32) * 5/9
        if t == 'k':
            return (v + 459.67) * 5/9
        if t == 'r':
            return v + 459.67
        if t == 'f':
            return v
    if f == 'k':
        if t == 'c':
            return v - 273.15
        if t == 'f':
            return v * 9/5 - 459.67
        if t == 'r':
            return v * 9/5
    if f == 'r':
        if t == 'c':
            return (v - 491.67) * 5/9
        if t == 'f':
            return v - 459.67
        if t == 'k':
            return v * 5/9
    return None

def conv_len(v, f, t):
    # units: m, cm, mm, km, in, ft
    try:
        v = float(v)
    except:
        return None
    # convert f to meters
    if f == 'm':
        meters = v
    elif f == 'cm':
        meters = v/100
    elif f == 'mm':
        meters = v/1000
    elif f == 'km':
        meters = v*1000
    elif f == 'in':
        meters = v*0.0254
    elif f == 'ft':
        meters = v*0.3048
    else:
        return None
    # back to t
    if t == 'm':
        return meters
    if t == 'cm':
        return meters*100
    if t == 'mm':
        return meters*1000
    if t == 'km':
        return meters/1000
    if t == 'in':
        return meters/0.0254
    if t == 'ft':
        return meters/0.3048
    return None

def conv_w(v, f, t):
    # units: kg, g, mg, lb
    try:
        v = float(v)
    except:
        return None
    if f == 'kg':
        kg = v
    elif f == 'g':
        kg = v/1000
    elif f == 'mg':
        kg = v/1e6
    elif f == 'lb':
        kg = v*0.45359237
    else:
        return None
    if t == 'kg': return kg
    if t == 'g': return kg*1000
    if t == 'mg': return kg*1e6
    if t == 'lb': return kg/0.45359237
    return None

def main():
    print("Welcome to LEGACY Universal Converter v0.0.1")
    typ = input("type (temp/len/w): ").strip()
    val = input("value: ").strip()
    f = input("from: ").strip()
    t = input("to: ").strip()
    if typ == 'temp':
        print(conv_temp(val,f,t))
    elif typ == 'len':
        print(conv_len(val,f,t))
    elif typ == 'w':
        print(conv_w(val,f,t))
    else:
        print("don't know")
if __name__ == '__main__':
    main()
