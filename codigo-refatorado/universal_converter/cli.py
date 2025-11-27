
import argparse
from .service import ConversionService

def parse_args():
    p = argparse.ArgumentParser(description='Universal Converter CLI')
    p.add_argument('value', help='numeric value to convert')
    p.add_argument('from_unit', help='unit to convert from (e.g. c, f, k, m, cm, kg, lb)')
    p.add_argument('to_unit', help='unit to convert to')
    return p.parse_args()

def main():
    args = parse_args()
    svc = ConversionService()
    out = svc.convert(args.value, args.from_unit, args.to_unit)
    if out is None:
        print("Conversion failed (invalid input or unit).")
    else:
        print(out)

if __name__ == '__main__':
    main()
